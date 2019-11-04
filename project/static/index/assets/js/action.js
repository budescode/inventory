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
		console.log(data)
		if (data.error){
			console.log('error')
			head = document.querySelector('.registerhead')
			head.innerHTML = data.error
			head.style.color = 'red'
		}
		else if(data.response){
		document.querySelector('.registerhead').innerHTML = "done"	
		document.location.reload(true)
		}
		
	})

	// console.log("clicked", inputemail, inputname, inputPassword)
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
			console.log(data.error)
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
	console.log(sexlist)
}

function changeSize(size){
	
	sizelist[0] = size
	console.log(sizelist)
}

function changeQuantity(quantity){
	
	quantitylist[0] = quantity
	console.log(quantitylist[0])
}

function addtoCartFunction(id){
	var token = document.querySelector("input[name=csrfmiddlewaretoken]").value
	error = document.querySelector('#error')
	error.style.display = 'none'
	sexlist1 = sexlist[0]
	sizelist1 = sizelist[0]
	quantitylist1 = quantitylist[0]
	if(sexlist1 == 'NONE'){		
		error.innerHTML = "please select sex"
		error.style.display = 'block'
	}
	else if(sizelist1 == "NONE"){
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
	formData.append('sex', sexlist1)
	formData.append('size', sizelist1)
	formData.append('quantity', quantitylist1)
	
	
	fetch(url,
	{
	body: new URLSearchParams(formData),
	method: 'post',
	headers:{
	'X-CSRFTOKEN': token
	}
	}).then(res => res.json()).then(function(data) {
		console.log('data')
		document.querySelector('#loading_cart').style.display = 'none'
		cart_count = document.querySelector('#cart_count')
		cart_count1 = Number(cart_count.innerHTML) + Number(quantitylist1)
		cart_count.innerHTML = cart_count1
	})
	}

}
