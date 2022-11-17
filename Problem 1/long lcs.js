function lcs(s) {
    if (!s.length) return '';
    let sh = s.reduce((x, y) => x.length <= y.length ? x : y),
        sm = sh.length;

    for (let i = sm; i > 0; i--) {
        for (let j = 0; j <= sm - i; j++) {
            let sb = sh.slice(j, i + j)
            if (s.every(st => st.includes(sb)))
                return sb;
        }
    }
    return '';
}

console.log(lcs(process.argv.slice(2)));
