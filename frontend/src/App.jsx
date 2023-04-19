import Search from "./components/Search";
import axios from "axios";
import React from "react";
import Text from "./components/Text";

function App() {
  const [data, setData] = React.useState({});
  const [render, setRender] = React.useState(false);

  function handleSubmit(query) {
    const headers = {
      "Content-Type": "text/plain", // Set the Content-Type header to text/plain for raw string data
    };
    axios
      .post("http://192.168.1.130:80/submit", query, { headers })
      .then((res) => {
        setData(res.data);
        setRender((prev) => {
          return !prev;
        });
      })
      .catch((err) => console.log(err));
  }

  return (
    <div className="big-container">
      <div className="App">
        <Search submit={handleSubmit} />
      </div>
      <div className="text-container">
        {render &&
          Object.keys(data).map((key, index) => {
            const natural = parseInt(key, 10);
            const num = natural + 1;
            toString(num);
            return (
              <Text
                key={index}
                website={`Website ${num}`}
                content={data[key]}
              />
            );
          })}
      </div>
    </div>
  );
}

export default App;
