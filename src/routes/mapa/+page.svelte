<script lang="ts">
  import CesiumViewer from "../../components/CesiumViewer.svelte"
</script>
<div class="pagina-fondo">
</div>
<style>
.background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -2;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  display: flex;
}
</style>
<Cesium/>