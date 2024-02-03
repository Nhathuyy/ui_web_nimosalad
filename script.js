document.addEventListener('DOMContentLoaded', function () {
    const scrollableItems = document.getElementById('scrollableItems');

    // Generate more than 12 items for testing scroll
    for (let i = 1; i <= 20; i++) {
        const item = document.createElement('div');
        item.classList.add('item');
        item.setAttribute('draggable', 'true');
        item.innerText = `Item ${i}`;
        item.style.backgroundColor = getRandomColor();
        scrollableItems.appendChild(item);
    }

    // Implement smooth drag-and-drop functionality
    let isDragging = false;
    let startX;
    let scrollLeft;

    scrollableItems.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.pageX - scrollableItems.offsetLeft;
        scrollLeft = scrollableItems.scrollLeft;
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        e.preventDefault();
        const x = e.pageX - startX;
        const walk = x - scrollLeft;
        scrollableItems.scrollLeft = scrollLeft - walk;
    });
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}    
// box 1 
