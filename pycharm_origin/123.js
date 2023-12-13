function get_diff_des(m,n){
    var dp_n = Array.from({ length: m }, () => Array(n).fill(0));

    for(j=1;j<n;j++){
        dp_n[0][j] = 1
        for (i=1;i<m;i++){
            dp_n[i][0]=1
            dp_n[i][j] = dp_n[i - 1][j] + dp_n[i][j - 1]
        }
    }
    console.log(dp_n)
}

get_diff_des(4,5)