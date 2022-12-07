import React, { Component } from "react";
import io from 'socket.io-client';
import { useAppStore } from '../appStore'

class Realtime extends Component {
  constructor(props) {
    super(props);
   
    this.state = {
      liveLocations: []
    };    
  }

  componentDidMount() {
    
      const socket = io.connect(process.env.REACT_APP_WS_URL);

      socket.on("connected", function(data){
          console.log("listening connected...");
          socket.emit("location_updates")
      });

      socket.on("streamTweets", function(data){
          console.log("listen streamTweets...");
          console.log(data.stream_result)
      });

      socket.on("location_updates", (data) => {
          console.log("listen location updates...");
          console.log(data)
          
          this.setState({
            liveLocations: data.map( x => {
              console.log(this.props.store.persons)
              let person = this.props.store.persons.find( p => p.id == x.person_id);
              return {
                ...x,
                person_name: person? `${ person.first_name } ${ person.last_name }` : "Undefined person",
                company_name: person? person.company_name : "Undefined company"
              }
            })
          });

      });

  }

  render() {
    return (
      this.state.liveLocations.length?
      (<div className="lists checkin-container">
        <ul>
            {this.state.liveLocations.map((location, index) => (
              <li key={index} >
                <h3>
                  {/* { location.creation_time.substring(0, 19) }: {location.person_name}  {location.longitude} {location.latitude}  */}
                  <i className="person-name">{location.person_name}</i>just checked in at {location.longitude} {location.latitude} 
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
      </div>):""
    );
  }
}
export default Realtime;
