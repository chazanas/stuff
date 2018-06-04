// var colors = [
// 	'rgb(255, 0, 0)',
// 	'rgb(255, 255, 0)',
// 	'rgb(0, 255, 0)',
// 	'rgb(0, 255, 255)',
// 	'rgb(0, 0, 255)',
// 	'rgb(255, 0, 255)'
// ];

var num_squares = 6;
var colors = randColors(num_squares);
var squares = document.querySelectorAll('.square');
var colorDisplay = document.querySelector('#colorDisplay');
var error = document.querySelector('#error');
var h1 = document.querySelector('h1');
var pickedColor = pickColor();
var replay = document.querySelector('#replay');
var easy = document.querySelector('#easy');
var hard = document.querySelector('#hard');
hard.classList.add('selected');
colorDisplay.textContent = pickedColor;

for(var i = 0; i < squares.length; i++){
	squares[i].style.backgroundColor = colors[i];
	squares[i].addEventListener('click', function() {
		if (this.style.backgroundColor === pickedColor) {
			error.textContent = 'Good boy!!';
			changeColors(pickedColor);
			h1.style.backgroundColor = pickedColor;
			replay.textContent = 'Play again';
		}
		else {
			this.style.backgroundColor = '#232323';
			error.textContent = 'Try Again';	
		}
	})
}

hard.addEventListener('click', function () {
	this.classList.add('selected');
	easy.classList.remove('selected');
	num_squares = 6;
	for(var i = 3; i < 6; i++){
		squares[i].style.display = 'block';
	}
	doReplay();
})

easy.addEventListener('click', function () {
	this.classList.add('selected');
	hard.classList.remove('selected');
	num_squares = 3;
	for(var i = 3; i < 6; i++){
		squares[i].style.display = 'none';
	}
	doReplay();
})

replay.addEventListener('click', function() {
	doReplay()
})

function doReplay() { 
	colors = randColors(num_squares);
	pickedColor = pickColor();
	colorDisplay.textContent = pickedColor;
	error.textContent = '';
	for (var i = 0; i < colors.length; i++){
		squares[i].style.backgroundColor = colors[i];
	}
	replay.textContent = 'New colors';
	h1.style.backgroundColor = 'steelblue';
}

function changeColors(color) {
	for(var i = 0; i < colors.length; i++){
		squares[i].style.backgroundColor = color;
	}
}

function pickColor() {
	var rdn = Math.floor(Math.random() * colors.length);
	return colors[rdn];
}

function randColors(size){
	var colors = [];
	var red;
	var green;
	var blue;
	for(var i = 0; i < size; i++){
		red = Math.floor(Math.random() * 256);
		green = Math.floor(Math.random() * 256);
		blue = Math.floor(Math.random() * 256);
		colors.push('rgb(' + red + ', ' + green + ', ' + blue + ')')
	}

	return colors;
}