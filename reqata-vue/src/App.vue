<template>
  <div id="app">
        <nav class="navbar navbar-expand-lg navbar-light bg-nav">
            <div class="container">
                <a class="navbar-brand" href="/">Регата</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavDropdown">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link " aria-current="page" href="{%url 'exercise-list3'%}">Список заданий</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'score_table'%}">Зачетная таблица</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/admin">Админка</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container main-content">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
@import'~bootstrap/dist/css/bootstrap.css'
</style>
