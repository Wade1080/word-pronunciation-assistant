function temp(e, n) {
    function n(r) {
        console.log(111)
    }


    n.n = e => {
        var t = e && e.__esModule ? () => e.default : () => e;
        return n.d(t, {
            a: t
        }),
            t
    }
    n.d = (e, t) => {
        for (var r in t)
            n.o(t, r) && !n.o(e, r) && Object.defineProperty(e, r, {
                enumerable: !0,
                get: t[r]
            })
    }
    n.n({})

}

temp({"name": "huangxi", "age": '1'}, {})