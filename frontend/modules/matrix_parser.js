export function getParsedMatrix(matrix){
    const labeledMatrix = [Array.from({ length: matrix[0].length+1 }, (_, i) => i)];
    matrix.forEach((row, rowIdx) => {
        labeledMatrix.push([rowIdx+1, ...row]);
    });
    return labeledMatrix.map(row => row.join('\t')).join('\n').replace("0", "");
}
