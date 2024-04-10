export function getParsedMatrix(matrix){
    const labeledMatrix = [Array.from({ length: matrix[0].length+1 }, (_, i) => i)];
    matrix.forEach((row, rowIdx) => {
        labeledMatrix.push([rowIdx+1, ...row]);
    });
    return labeledMatrix.map(row => row.join('\t')).join('\n').replace("0", "");
}

export function downloadMatrix(parsedMatrix, matrixType){
    const blob = new Blob([parsedMatrix], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');

    link.href = url;
    link.download = `${matrixType}-matrix.txt`;

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}
