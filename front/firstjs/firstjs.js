var but = document.getElementById('but');
var par = document.getElementById('change');

but.addEventListener('click', function() {
	if (par.textContent == 'Eu'){
		par.textContent = 'Amo';
	}
	else if (par.textContent == 'Amo'){
		par.textContent = 'Você';
	}
	else {
		par.textContent = 'Eu'
	}
})