<script>
    import video from '$lib/assets/animation.mp4';

</script>
<div class="background1">
  <h1>Immersive Lunar Explorer: VR + AI</h1>

  <p>
    Experience space as if you were truly there. This demo combines <strong>virtual reality</strong> with <strong>advanced artificial intelligence</strong> to deliver an immersive journey through the solar system—with a special focus on <strong>our Moon</strong>. Users navigate in <em>first-person perspective</em>, observing celestial bodies with a realistic and deeply engaging sense of presence.
  </p>

  <p>
    The experience features <strong>three real-time visualization modes</strong>:
  </p>
  <ul>
    <li><strong>Normal view</strong>: A faithful representation based on real imagery from space missions.</li>
    <li><strong>Infrared view</strong>: Reveals thermal activity and surface temperature variations across the lunar landscape.</li>
    <li><strong>NEO view (Near-Earth Objects)</strong>: Highlights asteroids and nearby objects, contextualizing their relationship with the Moon and Earth.</li>
  </ul>

  <p>
    At the core of this experience lies a specialized <strong>large language model (LLM)</strong> trained in astronomy, which generates <strong>dynamic, contextual descriptions in real time</strong>. As users explore craters, lunar maria, or polar regions, the AI explains what they’re seeing, answers natural-language questions, and tailors its explanations to the user’s knowledge level—whether they’re a curious beginner or a science enthusiast.
  </p>

  <p>
    More than just a visual tool, this project aims to deepen the emotional and intellectual connection with the Moon, sparking wonder, curiosity, and a genuine desire to learn. By making space science accessible, interactive, and visually captivating, the demo bridges the gap between lunar exploration and the public—encouraging greater immersion, understanding, and appreciation for our natural satellite.
  </p>
  <video src={video} controls width="90%" style="margin-right: 0;margin-left:0;">
  <track kind="captions" label="English captions" srcLang="en" src="" default />
</video>
</div>

<style>
.background1 {
    background-image: url('./Fondos/lunapagina2.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    min-height: 100vh;
    padding: 2rem;
    color: white;
}

.background1 p {
    line-height: 1.6;
    margin-bottom: 1.2rem;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}

.background1 h1 {
    margin-bottom: 1.2rem;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}
</style>