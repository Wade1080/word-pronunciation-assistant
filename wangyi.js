const crypto = require('crypto');
eTemp = {
    "le": "",
    "phonetic": "",
    "rate": 4,
    "word": "link",
    "type": "2",
    "id": ""
};
nTemp = 'U3uACNRWSDWdcsKm';
rTemp = 'voiceDictWeb';
oTemp = 'webdict';
sTemp = 'dick';

// 创建对象，t创建函数，t()构成闭包，返回上面传过来的e对象，t()(o) 是new 一个对象
var t = () => (e) => {

    console.log('e==========>', e)

    return function (t, n) {
        console.log('进来啦!!!!')
        const c_temp = new e.init(n).finalize(t)
        console.log(c_temp)
        return c_temp
    }
};

var i = () => {
    function stringify(e) {
        for (var t = e.words, n = e.sigBytes, r = [], o = 0; o < n; o++) {
            var i = t[o >>> 2] >>> 24 - o % 4 * 8 & 255;
            r.push((i >>> 4).toString(16)),
                r.push((15 & i).toString(16))
        }
        return r.join("")
    }

    function parse(e) {
        for (var t = e.length, n = [], r = 0; r < t; r += 2)
            n[r >>> 3] |= parseInt(e.substr(r, 2), 16) << 24 - r % 8 * 4;
        return new s.init(n, t / 2)
    }
}


function u(e, t) {
    var n = Object.keys(e);
    if (Object.getOwnPropertySymbols) {
        var r = Object.getOwnPropertySymbols(e);
        t = true;
        t && (r = r.filter((function (t) {
                return Object.getOwnPropertyDescriptor(e, t).enumerable
            }
        ))),
            n.push.apply(n, r)
    }
    return n
}

function l(e) {
    return l = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (e) {
            return typeof e
        }
        : function (e) {
            return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
        }
        ,
        l(e)
}


const s = function (e, n, r, o, s) {
    var c, d = arguments.length > 5 && void 0 !== arguments[5] ? arguments[5] : 1,
        p = arguments.length > 6 && void 0 !== arguments[6] ? arguments[6] : "web",
        h = arguments.length > 7 && void 0 !== arguments[7] ? arguments[7] : 1,
        f = arguments.length > 8 && void 0 !== arguments[8] ? arguments[8] : "web",
        b = arguments.length > 9 && void 0 !== arguments[9] ? arguments[9] : 1,
        m = arguments.length > 10 && void 0 !== arguments[10] ? arguments[10] : 1,
        v = arguments.length > 11 && void 0 !== arguments[11] ? arguments[11] : 1,
        g = arguments.length > 12 && void 0 !== arguments[12] ? arguments[12] : "wifi",
        y = arguments.length > 13 && void 0 !== arguments[13] ? arguments[13] : "abcdefg", _ = Object.assign({
            product: o,
            appVersion: d,
            client: p,
            mid: h,
            vendor: f,
            screen: b,
            model: m,
            imei: v,
            network: g,
            keyfrom: s,
            keyid: r,
            mysticTime: Date.now(),
            yduuid: y
        }, e), w = (c = function () {
            var e = arguments.length > 1 ? arguments[1] : void 0
                , n = function (e) {
                for (var t = 1; t < arguments.length; t++) {
                    var n = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? u(Object(n), !0).forEach((function (t) {
                            var r, o, i, a;
                            r = e,
                                o = t,
                                i = n[t],
                                a = function (e) {
                                    if ("object" != l(e) || !e)
                                        return e;
                                    var t = e[Symbol.toPrimitive];
                                    if (void 0 !== t) {
                                        var n = t.call(e, "string");
                                        if ("object" != l(n))
                                            return n;
                                        throw new TypeError("@@toPrimitive must return a primitive value.")
                                    }
                                    return String(e)
                                }(o),
                                (o = "symbol" == l(a) ? a : String(a)) in r ? Object.defineProperty(r, o, {
                                    value: i,
                                    enumerable: !0,
                                    configurable: !0,
                                    writable: !0
                                }) : r[o] = i
                        }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : u(Object(n)).forEach((function (t) {
                            Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t))
                        }
                    ))
                }
                return e
            }({}, arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {});
            Object.keys(n).forEach((function (e) {
                    "" === n[e] && delete n[e]
                }
            ));
            var r = Object.keys(n).sort().filter((function (e) {
                    return !(void 0 === n[e])
                }
            ));
            r.push("key"),
                n.key = e;
            var o = "".concat(r.map((function (e) {
                    return "".concat(e, "=").concat(n[e])
                }
            )).join("&"));
            return [t()(o).toString(i()), r.join(",")]
        }(_, n),
        function (e) {
            if (Array.isArray(e))
                return e
        }(c) || function (e) {
            var t = null == e ? null : "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
            if (null != t) {
                var n, r, i, o, a = [], u = !0, s = !1;
                try {
                    for (i = (t = t.call(e)).next; !(u = (n = i.call(t)).done) && (a.push(n.value),
                    2 !== a.length); u = !0)
                        ;
                } catch (e) {
                    s = !0,
                        r = e
                } finally {
                    try {
                        if (!u && null != t.return && (o = t.return(),
                        Object(o) !== o))
                            return
                    } finally {
                        if (s)
                            throw r
                    }
                }
                return a
            }
        }(c) || function (e) {
            if (e) {
                if ("string" == typeof e)
                    return a(e, 2);
                var t = Object.prototype.toString.call(e).slice(8, -1);
                return "Object" === t && e.constructor && (t = e.constructor.name),
                    "Map" === t || "Set" === t ? Array.from(e) : "Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t) ? a(e, 2) : void 0
            }
        }(c) || function () {
            throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }()), x = w[0], k = w[1];
    return Object.assign(_, {
        sign: x,
        pointParam: k
    }),
        _
};
console.log(s(eTemp, nTemp, rTemp, oTemp, sTemp))