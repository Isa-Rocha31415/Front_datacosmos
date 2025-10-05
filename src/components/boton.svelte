
<script>
  import './boton.css';
  export let text = "Ir a inicio";
  export let href = "/";
  export let color = "blue";
  export let newTab = false;
</script>


<a 
  href={href} 
  class="nav-button {color}"
  target={newTab ? '_blank' : null}
  rel={newTab ? 'noopener noreferrer' : null}
>
  {text}
</a>