const ratings = document.querySelectorAll('.rating')
const ratingsContainer = document.querySelector('.ratings-container')

const sendBtn = document.querySelector('#send')
const panel = document.querySelector('#panel')


let selectedRating = 'Satisfied'

ratingsContainer.addEventListener('click', (e) => {
    if(e.target.parentNode.classList.contains('rating')) {
        removeActive()
        e.target.parentNode.classList.add('active')
        selectedRating = e.target.nextElementSibling.innerHTML
    }
    if(e.target.classList.contains('rating')) {
        removeActive()
        e.target.classList.add('active')
        selectedRating = e.target.nextElementSibling.innerHTML
    }

})

sendBtn.addEventListener('click', (e) => {
    panel.innerHTML = `
        
        <b>Thank You!</b>
        
        <p>Feedback : ${selectedRating}</p>
        <p>We'll use your feedback to improve our performance and will try to keep on growing Exponentially...</p>

    
    `
})


function removeActive() {
    for(let i = 0; i < ratings.length; i++) {
        ratings[i].classList.remove('active')
    }
}

