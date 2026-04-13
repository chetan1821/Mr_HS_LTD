const counters = document.querySelectorAll('.counter');

counters.forEach(counter => {
    let count = 0;
    const target = parseInt(counter.innerText);

    const update = () => {
        const increment = target / 100;

        if (count < target) {
            count += increment;
            counter.innerText = Math.ceil(count) + "+";
            setTimeout(update, 20);
        } else {
            counter.innerText = target + "+";
        }
    };

    update();
});




