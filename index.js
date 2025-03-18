
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
        import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

        let scene, camera, renderer, controls, gorilla, clock, mixers = [];
        let startScreen, startButton;
        
        init();
        animate();

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.body.appendChild(renderer.domElement);

            controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;

            clock = new THREE.Clock();
            loadGorilla();

            const light = new THREE.DirectionalLight(0xffffff, 1);
            light.position.set(5, 5, 5).normalize();
            scene.add(light);
            const ambientLight = new THREE.AmbientLight(0x404040, 2);
            scene.add(ambientLight);

            createStartScreen(); // Create start screen
            
            window.addEventListener('resize', onWindowResize, false);
        }

        function createStartScreen() {
            startScreen = document.createElement('div');
            startScreen.id = 'start-screen';
            startScreen.innerHTML = `
                <h1>Gorilla Escape</h1>
                <p>Help Sergius escape from his captors and reclaim his freedom!</p>
                <button id="start-button">Start Game</button>
            `;
            document.body.appendChild(startScreen);

            startButton = document.getElementById('start-button');
            startButton.addEventListener('click', startGame);
        }

        function startGame() {
            document.body.removeChild(startScreen);
            camera.position.set(0, 2, 5);
        }

        function loadGorilla() {
            const loader = new GLTFLoader();
            loader.load('path/to/gorilla_model.glb', function (gltf) {
                gorilla = gltf.scene;
                gorilla.scale.set(0.5, 0.5, 0.5);
                scene.add(gorilla);
                if (gltf.animations.length) {
                    const mixer = new THREE.AnimationMixer(gorilla);
                    gltf.animations.forEach((clip) => {
                        mixers.push(mixer);
                        mixer.clipAction(clip).play();
                    });
                }
            });
        }

        function animate() {
            requestAnimationFrame(animate);
            const delta = clock.getDelta();
            mixers.forEach(mixer => mixer.update(delta));
            controls.update();
            renderer.render(scene, camera);
        }

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }
    