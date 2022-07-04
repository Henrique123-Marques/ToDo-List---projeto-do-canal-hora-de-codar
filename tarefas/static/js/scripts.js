$(document).ready(function() {
	
	var baseUrl = 'http://127.0.0.1:8000/';
	var searchBtn = $('#search-btn');
	var searchForm = $('#search-form');
	var filter = $('#filter');
	
	$(searchBtn).on('click', function() {
		searchForm.submit();
	});

	$(filter).change(function() {
		var filter = $(this).val();
		window.location.href = baseUrl + '?filter=' + filter;
	});
});