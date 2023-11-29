<template lang="pug">
q-layout(view="hHh Lpr lff").full-width
  CabecalhoPrincipal
  q-page-container
    router-view
</template>

<script>
import CabecalhoPrincipal from '../components/CabecalhoPrincipal.vue'


export default {
  name: 'PrincipalBusca',
  components: { CabecalhoPrincipal },
  data(){
    return{
    }
  }
}
</script>
