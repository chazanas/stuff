var app = {
	todos : []
}

$('input').css('display', 'none');

$('input').on('keypress', function(event) {
	var task = $(this).val()
	if(event.which == 13 && app.todos.indexOf(task) < 0 && task.length > 0){
		app.todos.push(task);
		$(this).val('');
		$('ul').append('<li><span><i class="far fa-trash-alt"></i></span> ' + task + '</li>');
	}
})


$('ul').on('click', 'li', function() {
	$(this).toggleClass('cut');
})

$('ul').on('click', 'li span', function(event) {
	$(this).parent().fadeOut(200, function() {
		$(this).remove();
		app.todos.pop()
	});
	event.stopPropagation();
})

$('.fa-plus').on('click', function() {
	$('input').fadeToggle(100);
})

