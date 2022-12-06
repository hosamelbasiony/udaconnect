import React, { Component } from "react";
import io from 'socket.io-client';

class Realtime extends Component {
  constructor(props) {
    super(props);
    // TODO: endpoint should be abstracted into a config variable

    this.state = {
      persons: [],
      liveLocations: [],
    };

    let messages = [];
    
    const socket = io.connect("http://127.0.0.1:5005/npTweet");
    console.log("http://127.0.0.1:5005/npTweet");
    // listen to the event 'connected'
    socket.on("connected", function(data){
        console.log("listening connected...");
        // socket.emit("startTweets")
        socket.emit("location_updates")
    });

    socket.on("streamTweets", function(data){
        console.log("listen streamTweets...");
        console.log(data.stream_result)
    });

    socket.on("location_updates", (data) => {
        console.log("listen location updates...");
        console.log(data)
        messages = [...data,...messages ]
        
        this.setState({
          liveLocations: data
        });
        // document.querySelector("#log").innerHTML = `<pre>${JSON.stringify(messages, undefined, 3)}</pre>`;
    });
    
  }

  componentDidMount() {
    // alert("componentDidMount")
  }

  render() {
    return (
      <div className="lists">
        <ul>
            {this.state.liveLocations.map((location, index) => (
              <li key={index} >
                <h3>
                  { location.creation_time.substring(0, 19) }: {location.person_name}  {location.longitude} {location.latitude} 
                </h3>
              </li>
            ))}
          </ul>                
        
          {/* {
            "person_id": 1,
            "longitude": "30.605240974982205",
            "latitude": "32.29687938288871",
            "creation_time": "2022-08-18 10:37:06.000000"
          } */}
      </div>
    );
  }
}
export default Realtime;
