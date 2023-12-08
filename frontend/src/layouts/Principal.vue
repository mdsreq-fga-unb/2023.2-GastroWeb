<template lang="pug">
q-layout(view="hHh Lpr lff").full-width
  CabecalhoPrincipal
  q-page-container
    router-view
</template>

<script>
import CabecalhoPrincipal from '../components/CabecalhoPrincipal.vue'
import { mapActions } from 'vuex'

export default {
  name: 'PrincipalBusca',
  components: { CabecalhoPrincipal },
  props: {
    titulo: String,
    categorias: [String, Array],
    tags: [String, Array],
    id: Number
  },
  data(){
    return{
    }
  },
  methods: {
    ...mapActions('busca', ['setParametrosBusca']),
    carregarPagina() {
      console.log(this.tags, this.categorias)
      this.setParametrosBusca({
        titulo: this.titulo || '',
        tags: this.arrayfy(this.tags),
        categorias: this.arrayfy(this.categorias),
        id: this.id || 0
      })
    },
    arrayfy (data) {
      return data
        ? Array.isArray(data)
          ? data
          : [ data ]
        : []
    }
  },
  mounted () {
    this.carregarPagina()
  }
}
</script>
