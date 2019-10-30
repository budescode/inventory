
// var delete_btn = document.querySelector("#delete_btn")
// delete_btn.addEventListener('click', deleteFunction)

function changeEditModal(id){
    document.querySelector('#editcatmodal_id').innerHTML = id
    document.querySelector('#editcategory_input').value = 0
}

function changeCategory(){
   id =  document.querySelector('#editcatmodal_id').innerHTML
   loadingid = '#editloading' + id
   document.querySelector(loadingid).style.display = 'block'
   editcategory_input =  document.querySelector('#editcategory_input').value
    var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
    var url = 'http://www.1kshop.online/administrator/editmycategory/'
    let  formData = new FormData()
    formData.append('editcategoryid', id)
    formData.append('edittotal', editcategory_input)
	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}
	}).then(res => res.json()).then(function(data) {
	   id = '#total' + data.editcategoryid
	    document.querySelector(id).innerHTML = data.edittotal
       loadingid = '#editloading' + data.editcategoryid
       document.querySelector(loadingid).style.display = 'none'
	})
}


function changeEditModal(id){
    document.querySelector('#editcatmodal_id').innerHTML = id
    document.querySelector('#editcategory_input').value = 0
}

function changeSubCategory(){
   id =  document.querySelector('#editcatmodal_id').innerHTML
   loadingid = '#editloading' + id
   document.querySelector(loadingid).style.display = 'block'
   editcategory_input =  document.querySelector('#editcategory_input').value
    var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
    var url = 'http://www.1kshop.online/administrator/editmysubcategory/'
    let  formData = new FormData()
    formData.append('editsubcategoryid', id)
    formData.append('edittotal', editcategory_input)
	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}
	}).then(res => res.json()).then(function(data) {
	    id = '#total' + data.editsubcategoryid
	    document.querySelector(id).innerHTML = data.edittotal
       loadingid = '#editloading' + data.editsubcategoryid
       document.querySelector(loadingid).style.display = 'none'
	})
}



function changeImg(){
document.querySelector("#main_img").src = this.src
}



function editItems(value){

	var id = value.slice(9)
	var stock1 = '#stock' + id
	var stock = document.querySelector(stock1).innerHTML


// 	document.querySelector('#editavail').value = stock
// 	console.log(stock)
	document.querySelector('.editsubmitbutton').id = id

}




function editMyItems(value){
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	var stock = document.querySelector('#editavail').value
	var url = 'http://www.1kshop.online/administrator/edititems/'
	let  formData = new FormData()
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
	var id  = data.product_id
	var stock1 = '#stock' + id
	document.querySelector(stock1).innerHTML = data.stock
	document.querySelector('#editavail').value = ''
	})
}



function addItems(){

document.querySelector('#loading').style.display = 'block'

var categoryIndex1 = document.querySelector('#add_select_category').selectedIndex;
var category =  document.querySelector('#add_select_category').options[categoryIndex1].text

var subcategoryIndex1 = document.querySelector('#add_sub_category').selectedIndex;
var subcategory =  document.querySelector('#add_sub_category').options[subcategoryIndex1].text

var additemdescription = document.querySelector('#additemdescription').value
var additemsize = document.querySelector('#additemsize').value

var additemprice = document.querySelector('#additemprice').value
var additemavailable = document.querySelector('#additemavailable').value

var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
var url = 'http://www.1kshop.online/administrator/additems/'
let  formData = new FormData()
formData.append('category', category)
formData.append('subcategory', subcategory)

formData.append('sex', additemdescription)
formData.append('size', additemsize)
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

if(data.error == 'Category and subcategory mismatch') {
    document.querySelector('#loading').style.display = 'block'
    document.querySelector('#loading').style.color = 'red'

    document.querySelector('#loading').innerHTML = 'Category and subcategory mismatch'
}
else{
document.location.reload(true)
}


})

}
// end addItems



//this function is to edit the items in the dashboard
function editMyItems1(){

var editcategoryid = document.querySelector('#editcategoryid').innerHTML
var editsubcategoryid = document.querySelector('#editsubcategoryid').innerHTML
var editsex = document.querySelector('#editsex').innerHTML.toUpperCase()

var editsize = document.querySelector('#editsize').innerHTML.toUpperCase()
var editstock = document.querySelector('#editstock').value

document.querySelector('#loading').style.display = 'block'
//console.log(editcategoryid, editsubcategoryid, editsex, editsize, editstock,'yahhhhh')
var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
var url = 'http://www.1kshop.online/administrator/editmyitems/'
let  formData = new FormData()
formData.append('editcategoryid', editcategoryid)
formData.append('editsubcategoryid', editsubcategoryid)

formData.append('editsex', editsex)
formData.append('editsize', editsize)
formData.append('editstock', editstock)

// formData.append('price', additemprice)
// formData.append('stock', additemavailable)

fetch(url,
{
body: new URLSearchParams(formData),
method: 'post',
headers:{
'X-CSRFTOKEN': token
}


}).then(res => res.json()).then(function(data) {

document.location.reload(true)



})

}
// end editItems






function addCategory(){

var category = document.querySelector('#addcategory').value
var stock = document.querySelector('#addstockavailable').value


var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
var url = 'http://www.1kshop.online/administrator/addtocategory/'
let  formData = new FormData()
formData.append('category', category)
formData.append('stock', stock)



fetch(url,
{
body: new URLSearchParams(formData),
method: 'post',
headers:{
'X-CSRFTOKEN': token
}


}).then(res => res.json()).then(function(data) {

document.location.reload(true)



})
}

function addSubCategory(){

var subcategory = document.querySelector('#addsubcategory').value

var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
var url = 'http://www.1kshop.online/administrator/addsubcategory/'
let  formData = new FormData()
formData.append('subcategory', subcategory)


fetch(url,
{
body: new URLSearchParams(formData),
method: 'post',
headers:{
'X-CSRFTOKEN': token
}


}).then(res => res.json()).then(function(data) {

document.location.reload(true)



})
}



function deleteMyitems(value){

var id = value.slice(11)
console.log(id)
var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
var url = 'http://www.1kshop.online/administrator/deletemyitems/'
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
    report = document.querySelector('#record')
    report.style.display = 'none'
    categoryid = '#category'+ value
    subcategoryid = '#subcategory'+ value
    sexid = '#sex'+ value
    sizeid = '#size'+ value
    category = document.querySelector(categoryid).innerHTML
    subcategory = document.querySelector(subcategoryid).value
    console.log(subcategory, 'yyyya')
    sex = document.querySelector(sexid).value
    size = document.querySelector(sizeid).value
	qty1 = '#qty'+value
	qty = document.querySelector(qty1).value
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	var url = 'http://www.1kshop.online/administrator/addtocart/'
	let  formData = new FormData()
	formData.append('post_pk', value)
	formData.append('qty', qty)
	formData.append('category', category)
	formData.append('subcategory', subcategory)
	formData.append('sex', sex)
	formData.append('size', size)
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
	    if (data.report == 'No Records found'){
	        report = document.querySelector('#record')
	        report.style.display = 'block'
            var id = '#img'+data.id
            document.querySelector(id).style.display = 'none'
	    }

	    else{
		var id = '#img'+data.id
		var id2 = '#stock'+data.id
		document.querySelector(id).style.display = 'none'
		document.querySelector('#cart_total').innerHTML = data.cart_total
		document.querySelector('.cart_total1').innerHTML = data.cart_total
		document.querySelector('.cart_price').innerHTML = data.total_price
		document.querySelector('.cart_price1').innerHTML = data.total_price
        stock = document.querySelector(id2).innerHTML
        stock1 = Number(stock) - Number(data.qty)
        document.querySelector(id2).innerHTML = stock1
	    }
	})
}



function editcartFunction(value, id){
	var qs = '#' + 'qt' + value
	var qty = document.querySelector(qs).value
	var img = '#editimg' + id
	var editimg = document.querySelector(img).style.display = 'block'
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	qty1 = '#'+value
	var url = 'http://www.1kshop.online/administrator/editcart/'
	let  formData = new FormData()
	formData.append('post_pk', value)
	formData.append('qty', qty)
	formData.append('id', id)
	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}


	}).then(res => res.json()).then(function(data) {
		console.log(data)
		var id = '#editimg'+data.id
		var input1 = '#qty'+data.id
		var single_price = '#single_price'+data.id
		var price = '#price'+ data.id
		document.querySelector(id).style.display = 'none'
		document.querySelector('#cart_total').innerHTML = data.cart_total
		document.querySelector('.cart_total1').innerHTML = data.cart_total

		document.querySelector('.cart_price').innerHTML = data.total_price
		document.querySelector('.cart_price1').innerHTML = data.total_price
		document.querySelector(price).innerHTML = data.price

		var input = document.querySelector(input1).value = data.qty
		var img = '#editimg' + data.id
		var editimg = document.querySelector(img).style.display = 'none'
		var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	})
}




function deletecartFunction(value){
	var id = '#img'+value
	document.querySelector(id).style.display = 'block'
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value

	var url = 'http://www.1kshop.online/administrator/deletecart/'
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
	var url = 'http://www.1kshop.online/administrator/viewdetails/'
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
