import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Particle Snow Background", page_icon="❄️", layout="wide")

# HTML for Particle Effect
particle_html = """
    <html>
        <head>
            <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
            <style>
                #particles-js {
                    position: fixed;
                    width: 100%;
                    height: 100%;
                    z-index: -1;
                }
                .particles-js-canvas-el {
                    display: inline;
                }
            </style>
        </head>
        <body>
            <div id="particles-js"></div>
            <script>
                particlesJS("particles-js", {
                    "particles": {
                        "number": {
                            "value": 80,
                            "density": {
                                "enable": true,
                                "value_area": 800
                            }
                        },
                        "color": {
                            "value": "#ffffff"
                        },
                        "shape": {
                            "type": "circle",
                            "stroke": {
                                "width": 0,
                                "color": "#000000"
                            },
                            "polygon": {
                                "nb_sides": 5
                            },
                            "image": {
                                "src": "img/github.svg",
                                "width": 100,
                                "height": 100
                            }
                        },
                        "opacity": {
                            "value": 0.5,
                            "random": false
                        },
                        "size": {
                            "value": 3,
                            "random": true
                        },
                        "move": {
                            "enable": true,
                            "speed": 6,
                            "direction": "none",
                            "random": false,
                            "straight": false,
                            "out_mode": "out"
                        }
                    },
                    "interactivity": {
                        "detect_on": "canvas",
                        "events": {
                            "onhover": {
                                "enable": true,
                                "mode": "repulse"
                            },
                            "onclick": {
                                "enable": true,
                                "mode": "push"
                            },
                            "resize": true
                        }
                    }
                });
            </script>
        </body>
    </html>
"""

# Display the particle effect using the HTML code
st.markdown(particle_html, unsafe_allow_html=True)

# Content of the Streamlit app
st.title("Welcome to My Streamlit App with Snowfall Effect!")
st.write("This background effect is powered by `particles.js`, providing a snowflake-like appearance.")

# Add more elements or features here as needed
st.button("Click Me!")
