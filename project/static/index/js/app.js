Vue.component("countdown", {
    template: `
        <ul class="countdown-time">
            <li>
                <!--Timer header and figure-->
                <p>Days</p>
                <figure>{{days}}</figure>
            </li>
            <li>
                <!--Timer header and figure-->
                <p>Hours</p>
                <figure>{{hours}}</figure>
            </li>
            <li>
                <!--Timer header and figure-->
                <p>Minutes</p>
                <figure>{{minutes}}</figure>
            </li>
            <li>
                <!--Timer header and figure-->
                <p>Seconds</p>
                <figure>{{seconds}}</figure>
            </li>
        </ul>
    `,
    props: {
        countDownDate: {
            type: String,
            default: 'Jan 5, 2021 15:37:25'
        }
    },
    data(){
        return{
            days: 0,
            hours: 0,
            minutes: 0,
            seconds: 0,
            stopInterval: false
        }
    },
    methods: {
        createCount() {
            // Get today's date and time
            var now = new Date().getTime();

            // Set the date we're counting down to
            var countDownDate = new Date(this.countDownDate).getTime();
            // Find the distance between now and the count down date
            var distance = countDownDate - now;

            // Time calculations for days, hours, minutes and seconds
            this.days = Math.floor(distance / (1000 * 60 * 60 * 24));
            this.hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            this.minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            this.seconds = Math.floor((distance % (1000 * 60)) / 1000);


            // If the count down is finished, stop the count
            if (distance <= 0) {
                this.stopTimer = true;
            }
        },
        
        /*
        **observeTabSwitch
        **@description: Check if the browser tab has been switched
        */
       observeTabSwitch(callback, intervalTime){
            var vm = this
            var hidden
            var visibilityChange
            if(typeof document.hidden !== "undefined"){
                hidden = "hidden"
                visibilityChange = "visibilitychange"
            }
            else if(typeof document.msHidden !== "undefined"){
                hidden = "msHidden"
                visibilityChange = "msvisibilitychange"
            }
            else if(typeof document.webkitHidden !== "undefined"){
                hidden = "webkitHidden"
                visibilityChange = "webkitvisibilitychange"
            }
            var startAutoplay = setInterval(()=>{
                callback()
            }, intervalTime)

            window.addEventListener(visibilityChange,function () {
                if(document[hidden] || vm.stopInterval === true) {
                    console.log('hidden')
                    return clearInterval(startAutoplay)
                } 
                console.log('shown')
                return startAutoplay = setInterval(()=>{
                    callback()
                }, intervalTime)
            })
        }
    },
    mounted(){
        return this.observeTabSwitch(()=>{
            this.createCount()
        },1000)
    }
})

var vue = new Vue({
    el: '#app'
})
