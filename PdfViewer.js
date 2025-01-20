import React from "react";
import { useLocation } from "react-router-dom";

const PdfViewer = () => {
    const location = useLocation();
    const { filePath } = location.state || {};

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h1>File Viewer</h1>
            {filePath ? (
                <iframe
                    src={`file:///${filePath}`}
                    title="File Viewer"
                    width="80%"
                    height="600px"
                    style={{ border: "1px solid #ccc" }}
                />
            ) : (
                <p>No file path provided.</p>
            )}
        </div>
    );
};

export default PdfViewer;
