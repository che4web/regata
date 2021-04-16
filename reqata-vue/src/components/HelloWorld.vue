<template>
    <div class="hello">
        <input v-model='search'> 
        <button v-on:click="setTask"> задача</button>
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div clas="col-3" v-for="item in exercise_list" :key="item.id">
                <exercise-card :item="item"/>
                </div>
            </div>
    </div>
</template>

<script>
import axios from 'axios'
import ExerciseCard from '../components/ExerciseCard'
export default {
        components:{
    ExerciseCard,
},
        name: 'exercise-list',
        data(){return {
            message: 'Привет, Vue!',
            search:'',
            exercise_list:[],
        }},
        watch:{
            search(){
                this.getExercise()
            }
        },
        mounted(){
            this.getExercise()
        },
        methods:{
            setTask(){
                this.message = "Задача"
            },
            async getExercise(){
                let response = await axios.get('/api/exercise/',{params:{search:this.search}})
                this.exercise_list = response.data
            
            }
        }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>
