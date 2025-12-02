import React, { useState } from "react";

function FileUpload({ onUpload }) {
  const [file, setFile] = useState(null);

  const uploadHandler = () => {
    if (file) {
      onUpload(file);
    }
  };

  return (
    <div style={{ padding: 10 }}>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button
        onClick={uploadHandler}
        style={{
          marginLeft: 10,
          padding: "6px 12px",
          border: "1px solid black",
          cursor: "pointer",
        }}
      >
        Upload
      </button>
    </div>
  );
}

export default FileUpload;
