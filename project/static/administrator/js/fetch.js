
// var delete_btn = document.querySelector("#delete_btn")
// delete_btn.addEventListener('click', deleteFunction)




function changeImg(){
document.querySelector("#main_img").src = this.src
}
 


function editItems(value){
	
	var id = value.slice(9)
	
	var category1 = '#category'+id
	var category = document.querySelector(category1).innerHTML
	var description1 = '#description' + id
	console.log(category)
	var description = document.querySelector(description1).innerHTML
	var price1 = '#price' + id
	var price = document.querySelector(price1).innerHTML

	var stock1 = '#stock' + id
	var stock = document.querySelector(stock1).innerHTML
	document.querySelector("#edititemscategory").innerHTML = category;
	document.querySelector("#edititemscategory").innerHTML = category;
	var categoryIndex = document.querySelector('#select_category').selectedIndex;
	document.querySelector('#select_category').options[categoryIndex].text = category
	document.querySelector('#editdescription').value = description
	document.querySelector('#editprice').value = price

	document.querySelector('#editavail').value = stock
	console.log(stock)
	document.querySelector('.editsubmitbutton').id = id
	
}




function editMyItems(value){
	console.log(value)
	// document.querySelector("#edititemscategory").innerHTML = category;
	// document.querySelector("#edititemscategory").innerHTML = category;
	// var categoryIndex = document.querySelector('#select_category').selectedIndex;
	// var category = document.querySelector('#select_category').options[categoryIndex].text 
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	var description = document.querySelector('#editdescription').value 
	var price = document.querySelector('#editprice').value 

	var stock = document.querySelector('#editavail').value 
	var categoryIndex1 = document.querySelector('#select_category').selectedIndex;
	var category =  document.querySelector('#select_category').options[categoryIndex1].text

	console.log(description, price, stock, category)

	var url = 'http://127.0.0.1:8000/edititems/'
	let  formData = new FormData()
	formData.append('category', category)
	formData.append('description', description)
	formData.append('price', price)
	formData.append('stock', stock)
	formData.append('product_id', value)
	
	fetch(url, 
	{
	body: new URLSearchParams(formData), 
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}


	}).then(res => res.json()).then(function(data) {


		console.log(data)
	var id  = data.product_id
	var category1 = '#category'+id
	document.querySelector(category1).innerHTML = data.category
	var description1 = '#description' + id

	document.querySelector(description1).innerHTML = data.description

	var price1 = '#price' + id
	document.querySelector(price1).innerHTML = data.price

	var stock1 = '#stock' + id
	document.querySelector(stock1).innerHTML = data.stock


	})
}

function addItems(){
	console.log('ok')
var categoryIndex1 = document.querySelector('#add_select_category').selectedIndex;
var category =  document.querySelector('#add_select_category').options[categoryIndex1].text
var additemdescription = document.querySelector('#additemdescription').value
var additemprice = document.querySelector('#additemprice').value
var additemavailable = document.querySelector('#additemavailable').value
console.log(category, additemdescription, additemprice, additemavailable)
var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
var url = 'http://127.0.0.1:8000/additems/'
let  formData = new FormData()
formData.append('category', category)
formData.append('description', additemdescription)
formData.append('price', additemprice)
formData.append('stock', additemavailable)

fetch(url, 
{
body: new URLSearchParams(formData), 
method: 'post',
headers:{
'X-CSRFTOKEN': token
}


}).then(res => res.json()).then(function(data) {

document.location.reload(true)
// 	console.log(data)
// // var id  = data.product_id
// // var classelem = '.post'+id
// // var tr = document.querySelector(classelem)
// // tr.remove()
// var tr = document.createElement('tr')
// var trclass = 'post'+data.product_id
// tr.className = trclass

// var td1 = document.createElement('td')
// var textnode1 = document.createTextNode(data.category)
// var a1 = document.createElement('a')
// var a1_id = 'category'+data.product_id
// // console.log(a1_id)
// a1.setAttribute('id', a1_id)
// // a1.id = a1_id


// a1.appendChild(textnode1)
// td1.appendChild(a1)

// var td2 = document.createElement('td')
// var span2 = document.createElement('span')
// var text2 = document.createTextNode(data.description)
// span2.id = 'description'+data.product_id

// span2.appendChild(text2)
// td2.appendChild(span2)

// var td3 = document.createElement('td')
// var span3 = document.createElement('span')
// var text3 = document.createTextNode(data.price)
// span3.id = 'description'+data.price

// span3.appendChild(text3)
// td3.appendChild(span3)

// var td4 = document.createElement('td')
// var button4 = document.createElement('button')
// button4.class = 'btn btn-primary btn-sm'
// button4.id = 'edititems' + data.product_id
// button4.setAttribute('data-toggle', "modal")
// button4.setAttribute('data-target', "#myModal")
// button4.onclick = editItems('edititems'+data.product_id)
// var i = document.createElement('i')
// i.className = 'fa fa-edit'

// button4.appendChild(i)
// td4.appendChild(button4)

// var td5 = document.createElement('td')
// var button5 = document.createElement('button')
// button5.class = 'btn btn-danger btn-sm'
// button5.id = 'deleteitems' + data.product_id
// button5.onclick = deleteMyitems('deleteitems'+data.product_id)
// var i2 = document.createElement('i')
// i2.className = 'fa fa-trash'

// button5.appendChild(i2)
// td5.appendChild(button5)

// tr.appendChild(td1)
// tr.appendChild(td2)
// tr.appendChild(td3)
// tr.appendChild(td4)
// tr.appendChild(td5)

// var tablebody = document.querySelector('#tablebody')
// tablebody.appendChild(tr)


})



}

function deleteMyitems(value){

var id = value.slice(11)
console.log(id)
var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
var url = 'http://127.0.0.1:8000/deletemyitems/'
let  formData = new FormData()
formData.append('product_id', id)

fetch(url, 
{
body: new URLSearchParams(formData), 
method: 'post',
headers:{
'X-CSRFTOKEN': token
}


}).then(res => res.json()).then(function(data) {


	console.log(data)
var id  = data.product_id
var classelem = '.post'+id
var tr = document.querySelector(classelem)
tr.remove()



})



}




function addtocartFunction(value){
	// console.log(value)
	// var data = "post"+value
	// var element = document.querySelector("[class= " +  data+ "]")
	// element.remove()
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	qty1 = '#qty'+value
	qty = document.querySelector(qty1).value
	// var token = document.querySelector("#token").value
	console.log(qty)
	var url = 'http://127.0.0.1:8000/addtocart/'
	let  formData = new FormData()
	formData.append('post_pk', value)
	formData.append('qty', qty)
	var id = '#img'+value
	document.querySelector(id).style.display = 'block'



	fetch(url, 
	{
	body: new URLSearchParams(formData), 
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}


	}).then(res => res.json()).then(function(data) {
		var id = '#img'+data.id
		document.querySelector(id).style.display = 'none'
		document.querySelector('#cart_total').innerHTML = data.cart_total
		document.querySelector('.cart_total1').innerHTML = data.cart_total
		document.querySelector('.cart_price').innerHTML = data.total_price
		document.querySelector('.cart_price1').innerHTML = data.total_price

		console.log(data)
	})
}



function editcartFunction(value){
	// console.log(value)
	// var data = "post"+value
	// var element = document.querySelector("[class= " +  data+ "]")
	// element.remove()'
	var img = '#editimg' + value.slice(3)
	var editimg = document.querySelector(img).style.display = 'block'
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	qty1 = '#'+value
	console.log(value.slice(3))
	qty = document.querySelector(qty1).value
	// var token = document.querySelector("#token").value
	// console.log(qty)
	var url = 'http://127.0.0.1:8000/editcart/'
	let  formData = new FormData()
	formData.append('post_pk', value.slice(3))
	formData.append('qty', qty)
	var id = value.slice(3,-1)
	console.log(id)
	// document.querySelector(id).style.display = 'block'



	fetch(url, 
	{
	body: new URLSearchParams(formData), 
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}


	}).then(res => res.json()).then(function(data) {
		console.log(data)
		var id = '#img'+data.id
		var input1 = '#qty'+data.id
		var single_price = '#single_price'+data.id
		var price = '#price'+ data.id
		document.querySelector(id).style.display = 'none'
		document.querySelector('#cart_total').innerHTML = data.cart_total
		document.querySelector('.cart_total1').innerHTML = data.cart_total

		document.querySelector('.cart_price').innerHTML = data.total_price
		document.querySelector('.cart_price1').innerHTML = data.total_price

		document.querySelector(single_price).innerHTML = data.single_price
		document.querySelector(price).innerHTML = data.price

		var input = document.querySelector(input1).value = data.qty
		var img = '#editimg' + data.id
		var editimg = document.querySelector(img).style.display = 'none'
		var token = document.querySelector("input[name=csrfmiddlewaretoken]").value

		console.log(data)
	})
}




function deletecartFunction(value){
	var id = '#img'+value
	document.querySelector(id).style.display = 'block'
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value

	var url = 'http://127.0.0.1:8000/deletecart/'
	let  formData = new FormData()
	formData.append('post_pk', value)




	fetch(url, 
	{
	body: new URLSearchParams(formData), 
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}


	}).then(res => res.json()).then(function(data) {
		document.querySelector('#cart_total').innerHTML = data.cart_total
		document.querySelector('.cart_total1').innerHTML = data.cart_total
		document.querySelector('.cart_price').innerHTML = data.total_price
		document.querySelector('.cart_price1').innerHTML = data.total_price


		var id = '#img'+data.id
		document.querySelector(id).style.display = 'none'
		var tr_id = '.post'+data.id 
		var tr = document.querySelector(tr_id)
		tr.remove()
		console.log(data)
	})
}




function viewDetails(value){
	
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	// var token = document.querySelector("#token").value
	console.log(value)
	var url = 'http://127.0.0.1:8000/administrator/viewdetails/'
	let  formData = new FormData()
	formData.append('post_pk', value)


	fetch(url, 
	{
	body: new URLSearchParams(formData), 
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}


	}).then(res => res.json()).then(function(data) {
		var qs = JSON.parse(data.data)
		var data = qs[0].fields
		var pk = qs.pk
		// var image = data.image
		var img_link = 'http://127.0.0.1:8000/media/'
		var img = img_link+ data.image
		

		document.querySelector("#post_img1").src = img
		// document.querySelector("#post_img1").src = img
		document.querySelector("#plan_img").src = img_link+data.plan
		document.querySelector("#main_img").src = img
		document.querySelector("#address").innerHTML = data.address
		document.querySelector("#property_type").innerHTML = data.Property_type
		document.querySelector("#Price").innerHTML = data.Price
		// document.querySelector("#user").innerHTML = data.Price
		document.querySelector("#Bedrooms").innerHTML = data.Bedrooms
		document.querySelector("#Bathrooms").innerHTML = data.Bathrooms
		document.querySelector("#Car_spaces").innerHTML = data.Car_spaces
		document.querySelector("#new_or_established").innerHTML = data.new_or_established

		document.querySelector("#Swimming_pool").innerHTML = data.Swimming_pool
		document.querySelector("#Garage").innerHTML = data.Garage
		document.querySelector("#Balcony").innerHTML = data.Balcony
		document.querySelector("#Outdoor_area").innerHTML = data.Outdoor_area
		document.querySelector("#Undercover_parking").innerHTML = data.Undercover_parking

		document.querySelector("#Shed").innerHTML = data.Shed
		document.querySelector("#Fully_fenced").innerHTML = data.Fully_fenced
		document.querySelector("#Outdoor_spa").innerHTML = data.Outdoor_spa
		document.querySelector("#Tennis_court").innerHTML = data.Tennis_court
		document.querySelector("#Ensuite").innerHTML = data.Ensuite

		document.querySelector("#DishWasher").innerHTML = data.DishWasher
		document.querySelector("#Study").innerHTML = data.Study
		document.querySelector("#Built_in_robes").innerHTML = data.Built_in_robes
		document.querySelector("#Alarm_system").innerHTML = data.Alarm_system
		document.querySelector("#Broadband").innerHTML = data.Broadband

		document.querySelector("#Floorboards").innerHTML = data.Floorboards
		document.querySelector("#Gym").innerHTML = data.Gym
		document.querySelector("#Rumpus_room").innerHTML = data.Rumpus_room
		document.querySelector("#Workshop").innerHTML = data.Workshop
		document.querySelector("#Air_conditioning").innerHTML = data.Air_conditioning

		document.querySelector("#Solar_panels").innerHTML = data.Solar_panels
		document.querySelector("#Heating").innerHTML = data.Heating
		document.querySelector("#High_energy_efficiency").innerHTML = data.High_energy_efficiency
		document.querySelector("#Water_tank").innerHTML = data.Water_tank
		document.querySelector("#Solar_hot_water").innerHTML = data.Solar_hot_water
	


	})
}
