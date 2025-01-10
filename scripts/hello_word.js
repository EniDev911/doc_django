console.log("hello world")
var buttons = document.querySelectorAll("button[data-md-color-scheme]")
buttons.forEach(function(button) {
	button.addEventListener("click", function() {
		document.body.setAttribute("data-md-color-switching", "")
		var attr = this.getAttribute("data-md-color-scheme")
		document.body.setAttribute("data-md-color-scheme", attr)
		var name = document.querySelector("#__code_0 code span.l")
		name.textContent = attr
		setTimeout(function() {
			document.body.removeAttribute("data-md-color-switching")
		})
	})
})