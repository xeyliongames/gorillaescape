// script.js
let scene, camera, renderer, gorilla, labFloor;

function init() {
    // Create scene
    scene = new THREE.Scene();
    
    // Create camera
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 100;

    // Create renderer
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Add lighting
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(0, 1, 1).normalize();
    scene.add(light);

    // Create lab floor
    const floorGeometry = new THREE.BoxGeometry(200, 1, 200);
    const floorMaterial = new THREE.MeshStandardMaterial({ color: 0x8B4513 }); // Brown color
    labFloor = new THREE.Mesh(floorGeometry, floorMaterial);
    labFloor.position.y = -1; // Set floor position
    scene.add(labFloor);

    // Create gorilla model
    createGorilla();

    // Handle window resize
    window.addEventListener('resize', onWindowResize, false);

    // Start animation
    animate();
}

function createGorilla() {
    // Create gorilla's body (torso)
    const torsoGeometry = new THREE.CylinderGeometry(10, 10, 40, 32);
    const torsoMaterial = new THREE.MeshStandardMaterial({ color: 0x8B4513 });
    const torso = new THREE.Mesh(torsoGeometry, torsoMaterial);
    
    // Create gorilla's head
    const headGeometry = new THREE.SphereGeometry(12, 32, 32);
    const headMaterial = new THREE.MeshStandardMaterial({ color: 0x8B4513 });
    const head = new THREE.Mesh(headGeometry, headMaterial);
    head.position.y = 25; // Position above torso

    // Create gorilla's arms
    const armGeometry = new THREE.CylinderGeometry(3, 3, 30, 32);
    const leftArm = new THREE.Mesh(armGeometry, torsoMaterial);
    const rightArm = leftArm.clone();
    leftArm.position.set(-15, 10, 0); // Position left arm
    rightArm.position.set(15, 10, 0); // Position right arm

    // Create gorilla's legs
    const legGeometry = new THREE.CylinderGeometry(4, 4, 40, 32);
    const leftLeg = new THREE.Mesh(legGeometry, torsoMaterial);
    const rightLeg = leftLeg.clone();
    leftLeg.position.set(-10, -30, 0); // Position left leg
    rightLeg.position.set(10, -30, 0); // Position right leg

    // Group gorilla parts
    gorilla = new THREE.Group();
    gorilla.add(torso);
    gorilla.add(head);
    gorilla.add(leftArm);
    gorilla.add(rightArm);
    gorilla.add(leftLeg);
    gorilla.add(rightLeg);

    // Set gorilla position
    gorilla.position.y = 0; // Position gorilla above the floor
    scene.add(gorilla);
}

function animate() {
    requestAnimationFrame(animate);
    gorilla.rotation.y += 0.01; // Add rotation to gorilla for a simple animation
    renderer.render(scene, camera);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

init();