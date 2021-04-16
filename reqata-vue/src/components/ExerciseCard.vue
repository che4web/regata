<template lang="pug">
div(class="card")
    img(:src="item.get_preview" class="card-img-top" alt="...")
    div(class="card-body")
        h5(class="card-title") {{item.name}})
        p(class="card-text") немножко текста
        div(input v-model="item.value"   class="from-control")
        button(class="btn btn-primary" v-on:click="saveAnswer(item,index)") Оветить
        div {{item.response}}
</template>
<script>
import axios from 'axios'
export default {
    name:'exercise-card',
    props:['item'],
    data(){
        return{
        }
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
    }


}
</script>
