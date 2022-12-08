import React, { Component } from "react";
import io from 'socket.io-client';
import moment from 'moment'

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

  mockCheckIn = () => {
    let longitude = (Math.round((Math.random()*360 - 180) * 1000)/1000).toString();
    let latitude = (Math.round((Math.random()*360 - 180) * 1000)/1000).toString();

    const randomIndex = Math.floor(Math.random() * this.props.store.persons.length);
    const person = this.props.store.persons[randomIndex];
    
    const payload = {
      person_id: person.id, 
      longitude,
      latitude,
      creation_time: moment(new Date()).format("YYYY-MM-DD HH:mm:ss.SSSSSS")
      // creation_time: "2022-08-18 10:37:06.000000"
    }

    fetch(`${process.env.REACT_APP_LOCATIONS_API_URL}/locations`, {
      method: 'POST', // or 'PUT'
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })
    .then((response) => response.json())
    .then((data) => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  };

  render() {
    return (
      this.state.liveLocations.length?
      (<div className="lists checkin-container" onClick={() => this.mockCheckIn()}>
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
        </div>):
        <div className="lists checkin-container" onClick={() => this.mockCheckIn()}>
          <h3 className="checkin-mock">Click here to mock random location checkin</h3>          
        </div>
    );
  }
}
export default Realtime;
