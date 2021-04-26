import { reactive } from 'vue'

let baseURL = "http://127.0.0.1:5000/";

let state = {
    playlist: reactive([]),
    async remove(index) {
        let song = this.playlist[index];
        if (index > -1)
            this.playlist.splice(index, 1);
        let response = await fetch(baseURL + "remove", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
            body: JSON.stringify(song),
        });
        if (response.status == 200){
            let result = await response.json()
            console.log(result);
        }
    },
    async init() {
        // try get playlist
        let response = await fetch(baseURL + "playlist",
        { credentials: 'include' });
        if (response.status == 200){
            let result = await response.json()
            result.forEach(song => {
                this.playlist.push(song);
            });
        }
    },
    add: function(song) {
        // add song to playlist and mark as not saved
        console.log(song);
        this.playlist.push(song);
        this.trysave(song);
    },
    trysave: async function(song){
        let response = await fetch(baseURL + "add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
            body: JSON.stringify(song),
        });
        if (response.status == 200){
            let result = await response.json()
            console.log(result);
        }
    },
}

state.init();

export default state;