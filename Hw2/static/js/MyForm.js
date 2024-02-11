function checkInput() {
    var eventInput = document.getElementById('event');
    var pattern = eventInput.getAttribute('pattern');
    var re = new RegExp(pattern);
    
    if(re.test(eventInput.value)) {
        eventInput.setCustomValidity('');
    } else {
        eventInput.setCustomValidity('Event must be alphanumeric');
    }
}
