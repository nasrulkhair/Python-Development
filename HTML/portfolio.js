document.addEventListener('DOMContentLoaded', () => {
    // Smooth fade-in effect on scroll
    const faders = document.querySelectorAll('.fade-in');
    const appearOptions = {
        threshold: 0.5,
        rootMargin: "0px 0px -100px 0px"
    };
    
    const appearOnScroll = new IntersectionObserver((entries, appearOnScroll) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('appear');
            appearOnScroll.unobserve(entry.target);
        });
    }, appearOptions);
    
    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });

    // Sticky header
    const header = document.querySelector('header');
    const navHeight = header.offsetHeight;
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > navHeight) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // File upload handling
    const uploadForm = document.querySelector('#upload form');
    const fileInput = document.querySelector('#file');
    const uploadStatus = document.createElement('p');
    uploadForm.appendChild(uploadStatus);

    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const file = fileInput.files[0];
        
        if (!file) {
            uploadStatus.textContent = 'Please select a file to upload.';
            uploadStatus.style.color = 'red';
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('upload.php', {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                uploadStatus.textContent = 'File uploaded successfully!';
                uploadStatus.style.color = 'green';
            } else {
                throw new Error('Upload failed');
            }
        } catch (error) {
            uploadStatus.textContent = 'Error uploading file. Please try again.';
            uploadStatus.style.color = 'red';
        }
    });
});
