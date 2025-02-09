function addanother() {
    var form = document.querySelector('form');
    var questionNumber = form.querySelectorAll('input[type="text"]').length - 2 + 1;
    var newQuestion = document.createElement('div');
    newQuestion.classList.add('form-group');
    newQuestion.innerHTML = `
                <label for="question${questionNumber}">Question ${questionNumber}</label>
                <input type="text" id="question${questionNumber}" name="question${questionNumber}" required placeholder="Enter question ${questionNumber}">
            `;
    form.insertBefore(newQuestion, form.querySelector('button'));

    if (questionNumber == 10) {
        document.querySelector('.add-question-btn').style.display = 'none';
    }
}