import React from "react";

export default function Text(props) {
  return (
    <div className="website-text">
      <h1 className="text">{props.website}</h1>
      <ul>
        {props.content.map((string, index) => {
          return (
            <li className="text" key={index}>
              {string}
            </li>
          );
        })}
      </ul>
    </div>
  );
}
