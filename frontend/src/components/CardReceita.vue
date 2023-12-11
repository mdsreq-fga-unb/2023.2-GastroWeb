<template>
  <div class="card" @click="$emit('click', id)">
    <div class="card-content">
      <div class="image-container">
        <img :src="foto" alt="Imagem Receita" class="recipe-image" />
      </div>
      <div class="text-column">
        <h4 class="recipe-title">{{ titulo }}</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardReceita',
  props: {
    titulo: String,
    id: Number,
    instrucoes: String,
    foto: String
  }
}
</script>

<style scoped>
.card {
  max-width: 800px;
  margin: 20px auto;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  background-color: #fff;
}

.card-content {
  display: flex;
}
.image-container {
  width: 40%;
  overflow: hidden;
}

.recipe-image {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.3s ease;
}

.text-column {
  flex: 1;
  padding: 20px;
}

.recipe-title {
  color: #222;
  font-family: 'Roboto', sans-serif;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.recipe-instructions {
  color: #555;
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  line-height: 1.6;
}

.card:hover .recipe-image {
  transform: scale(1.1);
}
</style>
