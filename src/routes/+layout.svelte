<script>
	import icon from '$lib/assets/icon.png';
  import Header from '$lib/components/header.svelte';
  import Footer from '$lib/components/footer.svelte';
</script>

<div class="layout">
  <Header />
  <main><slot /></main>
  <Footer />
</div>

<style>
  .layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  main {
    flex: 1;
  }
</style>