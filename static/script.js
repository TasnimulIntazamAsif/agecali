function calculateAge() {
    const birthDate = document.getElementById('birthDate').value;
    
    if (!birthDate) {
        alert('Please enter your birth date');
        return;
    }

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ birthDate: birthDate })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('years').textContent = data.years;
        document.getElementById('months').textContent = data.months;
        document.getElementById('days').textContent = data.days;
        document.getElementById('minutes').textContent = data.minutes;
        document.getElementById('zodiac').textContent = data.zodiac;
        
        const result = document.getElementById('result');
        result.classList.add('show');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while calculating age');
    });
} 