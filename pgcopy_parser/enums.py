from enum import Enum


class PGOid(Enum):
    """PGCopy OID Identifiers."""

    _int8 = 1016
    _interval = 1187
    _json = 199
    _jsonb = 3807
    _macaddr = 1040
    _macaddr8 = 775
    _numeric = 1231
    _oid = 1028
    _text = 1009
    _time = 1183
    _timestamp = 1115
    _timestamptz = 1185
    _timetz = 1270
    _uuid = 2951
    _varchar = 1015
    bool = 16
    bpchar = 1042
    bytea = 17
    char = 18
    cidr = 650
    date = 1082
    float4 = 700
    float8 = 701
    inet = 869
    int2 = 21
    int4 = 23
    int8 = 20
    interval = 1186
    json = 114
    jsonb = 3802
    macaddr = 829
    macaddr8 = 774
    numeric = 1700
    oid = 26
    text = 25
    time = 1083
    timestamp = 1114
    timestamptz = 1184
    timetz = 1266
    uuid = 2950
    varchar = 1043


class PGDataType(Enum):
    """PGCopy Data Types."""

    Bool = 0
    Oid = 1
    Serial2 = 2
    Serial4 = 3
    Serial8 = 4
    Int2 = 5
    Int4 = 6
    Int8 = 7
    Float4 = 8
    Float8 = 9
    Numeric = 10
    Text = 11
    Bytes = 12
    Json = 13
    Uuid = 14
    Date = 15
    Timestamp = 16
    Timestamptz = 17
    Time = 18
    Timetz = 19
    Interval = 20
    Inet = 21
    Cidr = 22
    Array = 23
    Macaddr = 24
    Macaddr8 = 25


PGOidToDType: dict[PGOid, PGDataType] = {
    # Associate oid with data type.
    PGOid._int8: PGDataType.Array,
    PGOid._interval: PGDataType.Array,
    PGOid._json: PGDataType.Array,
    PGOid._jsonb: PGDataType.Array,
    PGOid._macaddr: PGDataType.Array,
    PGOid._macaddr8: PGDataType.Array,
    PGOid._numeric: PGDataType.Array,
    PGOid._oid: PGDataType.Array,
    PGOid._text: PGDataType.Array,
    PGOid._time: PGDataType.Array,
    PGOid._timestamp: PGDataType.Array,
    PGOid._timestamptz: PGDataType.Array,
    PGOid._timetz: PGDataType.Array,
    PGOid._uuid: PGDataType.Array,
    PGOid._varchar: PGDataType.Array,
    PGOid.bool: PGDataType.Bool,
    PGOid.bpchar: PGDataType.Text,
    PGOid.bytea: PGDataType.Bytes,
    PGOid.char: PGDataType.Text,
    PGOid.cidr: PGDataType.Cidr,
    PGOid.date: PGDataType.Date,
    PGOid.float4: PGDataType.Float4,
    PGOid.float8: PGDataType.Float8,
    PGOid.inet: PGDataType.Inet,
    PGOid.int2: PGDataType.Int2,
    PGOid.int4: PGDataType.Int4,
    PGOid.int8: PGDataType.Int8,
    PGOid.interval: PGDataType.Interval,
    PGOid.json: PGDataType.Json,
    PGOid.jsonb: PGDataType.Json,
    PGOid.macaddr: PGDataType.Macaddr,
    PGOid.macaddr8: PGDataType.Macaddr8,
    PGOid.numeric: PGDataType.Numeric,
    PGOid.oid: PGDataType.Oid,
    PGOid.text: PGDataType.Text,
    PGOid.time: PGDataType.Time,
    PGOid.timestamp: PGDataType.Timestamp,
    PGOid.timestamptz: PGDataType.Timestamptz,
    PGOid.timetz: PGDataType.Timetz,
    PGOid.uuid: PGDataType.Uuid,
    PGOid.varchar: PGDataType.Text,
}


PGDataTypeLength: dict[PGDataType, int] = {
    # Length for current data type.
    PGDataType.Bool: 1,
    PGDataType.Oid: 4,
    PGDataType.Serial2: 2,
    PGDataType.Serial4: 4,
    PGDataType.Serial8: 8,
    PGDataType.Int2: 2,
    PGDataType.Int4: 4,
    PGDataType.Int8: 8,
    PGDataType.Float4: 4,
    PGDataType.Float8: 8,
    PGDataType.Numeric: -1,
    PGDataType.Text: -1,
    PGDataType.Bytes: -1,
    PGDataType.Json: -1,
    PGDataType.Uuid: 16,
    PGDataType.Date: 4,
    PGDataType.Timestamp: 8,
    PGDataType.Timestamptz: 8,
    PGDataType.Time: 8,
    PGDataType.Timetz: 12,
    PGDataType.Interval: 16,
    PGDataType.Inet: -1,
    PGDataType.Cidr: -1,
    PGDataType.Array: -1,
    PGDataType.Macaddr: 6,
    PGDataType.Macaddr8: 8,
}
