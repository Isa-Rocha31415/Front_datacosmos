<script lang="ts">
    import "./main.css";
    import luna from "../assets/Fondos/recortada.png"
    import NavButton from '../components/boton.svelte';

    import f1 from "../assets/Fondos/Fondo3.png";
</script>

<div class="background" style="background-image: url({f1});">
    <div class="left-block">
  <a href="mapa" class="nav-button blue">Mapa</a>    
    </div>
    <div class="right-block">
        <div class="luna-container">
            <img src={luna} alt="luna full" class="luna" />
            

            
        </div>
    </div>
</div>
