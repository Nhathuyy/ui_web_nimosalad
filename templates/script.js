 
// box 2

document.addEventListener('DOMContentLoaded', function () {
    const scrollableItems = document.getElementById('scrollableItems');

    // Function to add a new item
    function addNewItem() {
        const item = document.createElement('div');
        item.classList.add('item');
        item.innerText = ` ${scrollableItems.children.length + 1}`;
        item.style.backgroundColor = getRandomColor();

        scrollableItems.insertBefore(item, scrollableItems.firstChild);
        // item.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'start' });

        // Remove 'active' class from the previous active item
        const previousActive = document.querySelector('.item.active');
        if (previousActive) {
            previousActive.classList.remove('active');
        }

        // Add 'active' class to the new item
        item.classList.add('active');
    }

    // Generate more than 12 items for testing scroll
    for (let i = 1; i <= 20; i++) {
        addNewItem();
    }
    scrollableItems.style.overflowY = 'hidden';

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

    // Example: Add a new item every 2 seconds
    setInterval(addNewItem, 2000);
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
