var upA = document.getElementById('upA')
var upB = document.getElementById('upB')
var reset = document.getElementById('reset')
var scoreA = document.getElementById('A')
var scoreB = document.getElementById('B')
var max = document.getElementById('max')
var new_max = document.getElementById('new_max')

upA.addEventListener('click', function() {
	if ((Number(scoreA.textContent) < Number(max.textContent)) && (Number(scoreB.textContent) < Number(max.textContent))){
		scoreA.textContent++;
	}
	if (Number(scoreA.textContent) == Number(max.textContent)){
		scoreA.style.color = 'green';
	}
})

upB.addEventListener('click', function() {
	if ((Number(scoreA.textContent) < Number(max.textContent)) && (Number(scoreB.textContent) < Number(max.textContent))){
		scoreB.textContent++;
	}
	if (Number(scoreB.textContent) == Number(max.textContent)){
		scoreB.style.color = 'green';
	}
})

reset.addEventListener('click', function() {
	scoreA.textContent = '0'
	scoreB.textContent = '0'
	scoreB.style.color = ''
	scoreA.style.color = ''
})



new_max.addEventListener('change', function() {
	console.log('inp')
	max.textContent = new_max.value
})