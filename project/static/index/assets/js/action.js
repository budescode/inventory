
function signupFunction(){
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	url = '/account/register_user/'
	inputname = document.querySelector('#inputname').value
	inputemail = document.querySelector('#inputemail').value
	inputPassword = document.querySelector('#inputPassword').value
	document.querySelector('.registerhead').innerHTML = 'Loading....'



	let  formData = new FormData()
	formData.append('username', inputname)
	formData.append('email', inputemail)
	formData.append('password', inputPassword)

	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}
	}).then(res => res.json()).then(function(data) {
		if (data.error){

			head = document.querySelector('.registerhead')
			head.innerHTML = data.error
			head.style.color = 'red'
		}
		else if(data.response){
		document.querySelector('.registerhead').innerHTML = "done"
		document.location.reload(true)
		}

	})


}




function addToFavourite(id){
    document.querySelector('#loading_favourite').style.display = 'block'
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	url = '/addtoFavourite/'+ id + '/'
	let  formData = new FormData()
	formData.append('id', id)
	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}
	}).then(res => res.json()).then(function(data) {
	    document.querySelector('#loading_favourite').innerHTML = 'added'


	})


}


// this function will edit cart id for login users
function editQuantityCart(id){
    id1 = '#'  + 'edit_cart_select' + id
    edit_cart_select = document.querySelector(id1).value
    console.log(id1, edit_cart_select)
    document.querySelector('#editcart_id').value = id
    document.querySelector('#editcart_quantity').value = edit_cart_select
    formid = document.querySelector('#editcartForm')
    formid.submit()
}


// this function will edit cart id for anonymous
function editQuantityCart1(id){
    id1 = '#'  + 'edit_cart_select' + id
    edit_cart_select = document.querySelector(id1).value
    console.log(id1, edit_cart_select)
    document.querySelector('#editcart_id').value = id
    document.querySelector('#editcart_quantity').value = edit_cart_select
    formid = document.querySelector('#editcartForm')
    formid.submit()
}





function loginFunction(){
	inputusername = document.querySelector('#inputusername').value
	inputPassword2 = document.querySelector('#inputPassword2').value
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	url = '/account/login_user/'
	document.querySelector('.loginmodalhead').innerHTML = 'Loading....'
	let  formData = new FormData()
	formData.append('username', inputusername)
	formData.append('password', inputPassword2)

	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}
	}).then(res => res.json()).then(function(data) {
		if (data.error){

			head = document.querySelector('.loginmodalhead')
			head.innerHTML = data.error
			head.style.color = 'red'
		}
		else if(data.response){
		document.querySelector('.loginmodalhead').innerHTML = "done"
		document.location.reload(true)
		}

	})

}



sexlist = ['NONE']
sizelist = ['NONE']
quantitylist = ['NONE']


function changeSex(sex){

	sexlist[0] = sex
}

function changeSize(size){

	sizelist[0] = size
}

function changeQuantity(quantity){

	quantitylist[0] = quantity
}

function addtoCartFunction(id){
    product_style = document.querySelector('#product_style').value
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	error = document.querySelector('#error')
	error.style.display = 'none'

	sizelist1 = sizelist[0]
	quantitylist1 = quantitylist[0]
     if(sizelist1 == "NONE"){
		error.innerHTML = "please select size"
		error.style.display = 'block'
	}

	else if(quantitylist1 == 'NONE'){
		error.innerHTML = "please select quantity"
		error.style.display = 'block'
	}
	else{
	url = '/cart/addtocart/'
	document.querySelector('#loading_cart').style.display = 'block'



	let  formData = new FormData()
	formData.append('product_id', id)
	formData.append('size', sizelist1)
	formData.append('quantity', quantitylist1)
	formData.append('product_style', product_style)



	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}
	}).then(res => res.json()).then(function(data) {
	    if(data.error){
    	error = document.querySelector('#error')
    	error.style.display = 'block'
    	error.innerHTML = data.error
    	document.querySelector('#loading_cart').style.display = 'none'
	    }
	    else{
    	error = document.querySelector('#error')
    	error.style.display = 'none'
		document.querySelector('#loading_cart').style.display = 'none'
		cart_count = document.querySelector('#cart_count')
		cart_count1 = Number(cart_count.innerHTML) + Number(quantitylist1)
		cart_count.innerHTML = cart_count1
	    }
	})
	}

}


function buyNowFunction(){
	error = document.querySelector('#error')
	error.style.display = 'none'

	sizelist1 = sizelist[0]
	quantitylist1 = quantitylist[0]
     if(sizelist1 == "NONE"){
		error.innerHTML = "please select size"
		error.style.display = 'block'
	}

	else if(quantitylist1 == 'NONE'){
		error.innerHTML = "please select quantity"
		error.style.display = 'block'
	}
	else{
    document.querySelector('#buynowformsize').value = sizelist1
    document.querySelector('#buynowformquantity').value = quantitylist1
    document.querySelector('#buynowform').submit()

	}

}


//this function is used to change the product image when the little images are clicked
function ChangeProductImage(image, color, id){
    main_id = '.' + 'product_id'
    product_id = document.querySelector(main_id)
    product_id.id = id;
    buy_now_id1 = '#product_id'
    document.querySelector(buy_now_id1).value = id
    document.querySelector('#product_image').src = image;
  product_style = document.querySelector('#product_style').value = color
}

//this function is used to chaange the product image when select changes
function changepImage(){
    id = '.' + 'product_id'
    product_id = document.querySelector(id)
    buy_now_id1 = '#product_id'

    product_style = document.querySelector('#product_style').value
    for(i=0; i<product_color.length; i++){
      if(product_color[i].color == product_style){
           document.querySelector('#product_image').src = '/media/' +  product_color[i].image;
           product_id.id = product_color[i].id;
           document.querySelector(buy_now_id1).value = product_color[i].id;

      }

    }



}


