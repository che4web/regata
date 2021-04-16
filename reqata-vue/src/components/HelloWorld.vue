<template>
    <div class="hello">
        <input v-model='search'> 
        <button v-on:click="setTask"> задача</button>
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div clas="col-3" v-for="item,index in exercise_list" :key="item.id">
                <div class="card" >
                    <img :src="item.get_preview" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{{item.name}}</h5>
                        <p class="card-text"> немножко текста</p>
                        <div > <input v-model="item.value"   class="from-control"> </div>
                        <button class="btn btn-primary" v-on:click="saveAnswer(item,index)">Оветить</button>
                        <div >{{item.response}}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
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
            async saveAnswer(item,index){
                let answer ={
                    exercise:item.id,
                    value:item.value,
                }
                let response = await axios.post('/api/answer/',answer)
                item.response = 'ваш ответ принять id:' +response.data.id
                this.$set(this.exercise_list,index,item)
            
            },
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
