import functools
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Generic, Literal, Optional, Sequence, TypeVar, final

# from mcdp_utils_misc import BoolLike, not_true

__all__ = [
    "ComposeList",
    "Coords",
    "CoordsComp",
    "CoordsConcreteOp",
    "CoordsConst",
    "CoordsIdentity",
    # "InvalidCoords",
    # "c_comp",
    # "c_comp_find",
    # "c_const",
    # "c_id",
    # "c_identity_product",
    # "c_ins",
    # "c_list",
    # "c_n_copies",
    # "c_reverse_tuple",
    # "cco_coords",
    # "cco_list",
    # "cco_tuple",
    # "check_same_coords",
    # "check_valid_coords",
    # "get_coords_length",
    # "is_2_el_permutation",
    # "is_valid_coords",
    # "same_coords",
]

X = TypeVar("X")
TM = tuple[X, ...]


@dataclass
class CoordsIsConstant:
    constant: object


class CoordsConcreteOp(Generic[X], ABC):
    @final
    def reduce_seq(self, seq: Sequence[X], /) -> X:
        return self._reduce_seq(seq)

    @abstractmethod
    def _reduce_seq(self, seq: Sequence[X], /) -> X:
        raise NotImplementedError()

    @final
    def reduce_const(self, value: X, /) -> X:
        return self._reduce_const(value)

    @abstractmethod
    def _reduce_const(self, value: X, /) -> X:
        raise NotImplementedError()

    @final
    def slice(self, x: X, i: int, ntot: int, /) -> X:
        return self._slice(x, i, ntot)

    @abstractmethod
    def _slice(self, x: X, i: int, ntot: int, /) -> X:
        raise NotImplementedError()


class CoordsInterface(ABC):
    @final
    def get_it(self, x: X, /, *, cco: CoordsConcreteOp[X]) -> X:
        return self._get_it(x, cco=cco)

    # @final
    # def is_constant(self, *, cco: CoordsConcreteOp[X]) -> Optional[CoordsIsConstant]:
    #     res = self._is_constant(cco=cco)
    #     if res is not None:
    #         check_isinstance(res, CoordsIsConstant, me=self, cco=cco)
    #     return res

    # @abstractmethod
    # def _is_constant(self, *, cco: CoordsConcreteOp[X]) -> Optional[CoordsIsConstant]:
    #     ...

    @abstractmethod
    def _get_it(self, x: X, /, *, cco: CoordsConcreteOp[X]) -> X:
        ...

    # @abstractmethod
    # def is_identity_for(self, F: Any) -> BoolLike:
    #     ...

    # @abstractmethod
    # def unwrap(self, A: int) -> "tuple[Literal[True], Coords] | tuple[Literal[False], None]":
    # #     ...

    # @abstractmethod
    # def wrap(self, i: int, n: int) -> "Coords":
    #     raise NotImplementedError()

    # @final
    # def apply(self, i2: "Coords", /, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     res = self._apply(i2, cco=cco)
    #     if not (why := is_valid_coords(res)):
    #         msg = "Invalid coords produced"
    #         raise InvalidCoords(msg, me=self, i2=i2, cco=cco, res=res, why=why)

    #     return res

    # @abstractmethod
    # def _apply(self, i2: "Coords", /, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     raise NotImplementedError()

    # @final
    # def simplify(self, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     res = self._simplify(cco=cco)
    #     if __debug__:
    #         check_valid_coords(res)
    #     return res

    # @abstractmethod
    # def _simplify(self, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     raise NotImplementedError()

    # @abstractmethod
    # def canonical_listfirst(self) -> "Coords":
    #     """
    #     Makes sure that the ComposeList is outside the CoordsComp.

    #     CoordsComp(0, 1, ComposeList((CoordsIdentity()))))

    #     becomes

    #     ComposeList((CoordsComp(0, 1, CoordsIdentity())))

    #     :return:
    #     """

    # @abstractmethod
    # def is_permutation(self) -> Optional[TM[int]]:
    #     """
    #     Returns the permutation as indices.

    #     Note that for CoordsIdentity(), it returns none.

    #     """

    # @final
    # # @lru_cache_method_single
    # def get_input_shape(self) -> Optional[TM[Any]]:
    #     return self._get_input_shape()

    # @abstractmethod
    # def _get_input_shape(self) -> Optional[TM[Any]]:
    #     ...


@dataclass(frozen=True, slots=True)
class CoordsIdentity(CoordsInterface):
    # def _get_input_shape(self) -> Optional[TM[Any]]:
    #     return None

    # def canonical_listfirst(self) -> "Coords":
    #     return self

    # def _is_constant(self, *, cco: CoordsConcreteOp[X]) -> Optional[CoordsIsConstant]:
    #     return None

    # def _apply(self, i2: "Coords", /, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     return i2

    # def wrap(self, i: int, n: int) -> "Coords":
    #     return c_ins(i, n, self)

    # def is_identity_for(self, F: Any) -> BoolLike:
    #     return True

    # def unwrap(self, A: int) -> "tuple[Literal[False], None]":
    #     return False, None

    def _get_it(self, x: X, /, *, cco: CoordsConcreteOp[X]) -> X:
        return x

    # def _simplify(self, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     return self

    # def is_permutation(self) -> Optional[TM[int]]:
    #     return None


@dataclass(frozen=True, slots=True)
class CoordsConst(CoordsInterface):
    value: object

    # def _get_input_shape(self) -> Optional[TM[Any]]:
    #     return None

    # def _is_constant(self, *, cco: CoordsConcreteOp[X]) -> CoordsIsConstant:
    #     return CoordsIsConstant(cco.reduce_const(self.value))

    def canonical_listfirst(self) -> "Coords":
        return self

    # def _apply(self, i2: "Coords", /, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     return self

    # def wrap(self, i: int, n: int) -> "Coords":
    #     return self
    #     # return c_ins(i, n, self)  # maybe just self?

    # def is_identity_for(self, F: Any) -> BoolLike:
    #     return False

    # def unwrap(self, A: int) -> "tuple[Literal[False], None]":
    #     return False, None

    def _get_it(self, x: X, /, *, cco: CoordsConcreteOp[X]) -> X:
        return cco.reduce_const(self.value)  # type: ignore

    # def _simplify(self, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     return self

    # def is_permutation(self) -> Optional[TM[int]]:
    #     return None


@dataclass(frozen=True, slots=True)
class CoordsComp(CoordsInterface):
    index: int
    ntot: int = field(compare=False)
    rest: "Coords"

    # def __post_init__(self):
    #     if self.ntot is None:
    #         raise ZValueError(me=self)

    # def _get_input_shape(self) -> Optional[TM[Any]]:
    #     basic = [None] * self.ntot
    #     # noinspection PyTypeChecker
    #     basic[self.index] = self.rest.get_input_shape()
    #     return tuple(basic)

    # def _is_constant(self, *, cco: CoordsConcreteOp[X]) -> Optional[CoordsIsConstant]:
    #     return self.rest.is_constant(cco=cco)

    # def _apply(self, i2: "Coords", /, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     if isinstance(i2, ComposeList):
    #         if self.ntot is not None:
    #             if len(i2.components) != self.ntot:
    #                 msg = f"Expected a sequence of length {self.ntot}"
    #                 raise ZValueError(msg, me=self, i2=i2)
    #             # assert len(i2.components) == self.ntot

    #         return self.rest.apply(i2.components[self.index], cco=cco)
    #     elif isinstance(i2, CoordsComp):
    #         return CoordsComp(index=i2.index, ntot=i2.ntot, rest=self.apply(i2.rest, cco=cco))
    #     elif isinstance(i2, CoordsIdentity):
    #         return self
    #     elif isinstance(i2, CoordsConst):
    #         #
    #         # if self.ntot is not None:
    #         #     if len(i2.value) != self.ntot:
    #         #         msg = f"Expected a sequence of length {self.ntot}"
    #         #         raise ZValueError(msg, me=self, i2=i2)
    #         v0 = cco.reduce_const(i2.value)  # type: ignore
    #         value_i = cco.slice(v0, self.index, self.ntot)
    #         val = CoordsConst(value_i)
    #         return self.rest.apply(val, cco=cco)

    #     else:
    #         raise ZValueError("Invalid type", me=self, i2=i2)

    # def wrap(self, i: int, n: int) -> "Coords":
    #     return c_ins(i, n, self)

    if __debug__:

        def __post_init__(self) -> None:
            # if not isinstance(self.ntot, int):
            #     raise ZAssertionError("ntot should be an int", me=self)
            assert isinstance(self.index, int)
            # assert isinstance(self.ntot, int)

            if self.ntot is not None:
                assert isinstance(self.ntot, int)
                assert 0 <= self.index < self.ntot, (self.index, self.ntot)
            check_valid_coords(self.rest)

    # if self.ntot is None:
    #     raise ZAssertionError("ntot is None", me=self)

    def _get_it(self, x: X, /, *, cco: CoordsConcreteOp[X]) -> X:
        # v = self.rest._get_it(x[self.index], reducer=reducer, const_reducer=const_reducer)
        # if __debug__:
        #     if self.ntot is not None:
        #         if len(x) != self.ntot:
        #             msg = "Expected a sequence of length %d, got %s" % (self.ntot, len(x))
        #             raise ZValueError(msg, me=self, x=x, reducer=reducer, const_reducer=const_reducer)
        val = cco.slice(x, self.index, self.ntot)
        return self.rest.get_it(val, cco=cco)  # type: ignore

    # def is_identity_for(self, F: Any) -> BoolLike:
    #     return False

    # def unwrap(self, A: int) -> "tuple[Literal[True], Coords] | tuple[Literal[False], None]":
    #     if self.index == A:
    #         return True, self.rest
    #     else:
    #         return False, None

    # def _simplify(self, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     # CoordsComp(index=0, ntot=1, rest=ComposeList(components=(CoordsIdentity(),)))
    #     if self.index == 0 and self.ntot == 1 and self.rest == ComposeList(components=(CoordsIdentity(),)):
    #         return CoordsIdentity()

    #     rest = self.rest.simplify(cco=cco)
    #     if rest is not self.rest:
    #         return CoordsComp(index=self.index, ntot=self.ntot, rest=rest)
    #     else:
    #         return self

    # def canonical_listfirst(self) -> "Coords":
    #     if isinstance(self.rest, ComposeList):
    #         components = tuple(
    #             CoordsComp(index=self.index, ntot=self.ntot, rest=rest.canonical_listfirst()) for rest in self.rest.components
    #         )

    #         return ComposeList(components)
    #     else:
    #         return CoordsComp(index=self.index, ntot=self.ntot, rest=self.rest.canonical_listfirst())

    # def is_permutation(self) -> Optional[TM[int]]:
    #     return None


# def join_shape(shape1: Optional[TM[Any]], shape2: Optional[TM[Any]]) -> Optional[TM[Any]]:
#     if shape1 is None:
#         return shape2
#     elif shape2 is None:
#         return shape1
#     elif shape1 == shape2:
#         return shape1
#     assert isinstance(shape1, tuple)
#     assert isinstance(shape2, tuple)
#     if len(shape1) != len(shape2):
#         raise ZException("Cannot join shapes", shape1=shape1, shape2=shape2)

#     return tuple(join_shape(s1, s2) for s1, s2 in zip(shape1, shape2))


# def join_shapes(shapes: tuple[Optional[TM[Any]], ...]) -> Optional[TM[Any]]:
#     return functools.reduce(join_shape, shapes, None)


@dataclass(frozen=True, slots=True)
class ComposeList(CoordsInterface):
    # def _get_input_shape(self) -> Optional[TM[Any]]:
    #     shapes = tuple(c.get_input_shape() for c in self.components)
    #     return join_shapes(shapes)

    # def canonical_listfirst(self) -> "Coords":
    #     return self

    # def _is_constant(self, *, cco: CoordsConcreteOp[X]) -> Optional[CoordsIsConstant]:
    #     sofar = []
    #     for c in self.components:
    #         if ok := c.is_constant(cco=cco):
    #             sofar.append(ok.constant)
    #         else:
    #             return None
    #     return CoordsIsConstant(cco.reduce_seq(sofar))

    # def _apply(self, i2: "Coords", /, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     components = tuple(c.apply(i2, cco=cco) for c in self.components)
    #     return cco.reduce_seq(components)

    components: "tuple[Coords, ...]"

    if __debug__:

        def __post_init__(self) -> None:
            assert isinstance(self.components, tuple)
            for c in self.components:
                check_valid_coords(c)

    # def wrap(self, i: int, n: int) -> "Coords":
    #     return ComposeList(components=tuple(c.wrap(i, n) for c in self.components))

    def _get_it(self, x: X, /, *, cco: CoordsConcreteOp[X]) -> X:
        inside = tuple(c.get_it(x, cco=cco) for c in self.components)
        return cco.reduce_seq(inside)

    # @classmethod
    # def from_seq(cls, seq: "Sequence[Coords]") -> "ComposeList":
    #     return cls(tuple(seq))

    # def __getitem__(self, item: int) -> "Coords":
    #     return self.components[item]

    # def __len__(self) -> int:
    #     return len(self.components)

    # def is_identity_for(self, F: Any) -> BoolLike:
    #     from .composition import is_iterable

    #     if not is_iterable(F):
    #         return False
    #         # raise ZAssertionError(msg, F=F, coords=coords)
    #     if len(self.components) != len(F):
    #         return False
    #     for i, c in enumerate(self.components):
    #         ok, unwrapped = c.unwrap(i)
    #         if not ok:
    #             return False
    #         if unwrapped is None:
    #             return False  # XXX: untested
    #         ok2 = unwrapped.is_identity_for(F[i])
    #         if not ok2:
    #             return False

    #     return True

    # def is_permutation(self) -> Optional[TM[int]]:
    #     i2j = []
    #     for i, c in enumerate(self.components):
    #         if not isinstance(c, CoordsComp):
    #             return None
    #         if c.rest != CoordsIdentity():
    #             return None
    #         i2j.append(c.index)

    #     njs = len(set(i2j))
    #     if njs != len(i2j):
    #         return None
    #     return tuple(i2j)

    # def unwrap(self, A: int) -> "tuple[Literal[True], Coords] | tuple[Literal[False], None]":
    #     subs: list[Coords] = []
    #     for i, c in enumerate(self.components):
    #         ok, coords_i = c.unwrap(A)
    #         if not ok:
    #             return False, None
    #             # return not_true("cannot unwrap", dict(A=A, coords=self, i=i, c=c, ok=ok)), None
    #         assert coords_i is not None
    #         subs.append(coords_i)
    #     return True, ComposeList(tuple(subs))

    # def _simplify(self, *, cco: "CoordsConcreteOp[Coords]") -> "Coords":
    #     if not self.components:
    #         return self
    #     changed = False
    #     subs: list[Coords] = []
    #     for c in self.components:
    #         c2 = c.simplify(cco=cco)
    #         subs.append(c2)
    #         if c2 is not c:
    #             changed = True
    #     if changed:
    #         return ComposeList(tuple(subs)).simplify(cco=cco)
    #     if all(isinstance(c, CoordsComp) for c in self.components):
    #         adds = [(c.index, c.ntot) for c in self.components]
    #         inside = [c.rest for c in self.components]

    #         if len(set(adds)) == 1:
    #             index, ntot = adds[0]
    #             return CoordsComp(index=index, ntot=ntot, rest=ComposeList(tuple(inside))).simplify(cco=cco)

    #         indices = [c.index for c in self.components]
    #         ntots = [c.ntot for c in self.components]
    #         N = len(self.components)
    #         if indices == list(range(N)) and ntots == [N] * N:
    #             if all(isinstance(_, CoordsIdentity) for _ in inside):
    #                 return CoordsIdentity()

    #     return self


Coords = CoordsIdentity | CoordsComp | ComposeList | CoordsConst


class CCOList(CoordsConcreteOp[object]):
    def _reduce_seq(self, seq: Sequence[object], /) -> object:
        return list(seq)

    def _reduce_const(self, value: object, /) -> object:
        return value

    def _slice(self, x: Any, i: int, ntot: Optional[int], /) -> object:
        if ntot is not None:
            n = len(x)
            if n != ntot:
                raise ValueError(
                    f"Expected {ntot} elements, got {n}",
                )
        return x[i]


cco_list = CCOList()


class CCOTupleSimple(CoordsConcreteOp[object]):
    def _reduce_seq(self, seq: Sequence[Any], /) -> object:
        return tuple(seq)

    def _reduce_const(self, value: object, /) -> object:
        return value

    def _slice(self, x: Any, i: int, ntot: Optional[int], /) -> object:
        if ntot is not None:
            n = len(x)
            if n != ntot:
                raise ValueError(f"Expected {ntot} elements, got {n}")
        return x[i]


def check_valid_coords(coords: "Coords") -> None:
    if not (why := is_valid_coords(coords)):
        raise InvalidCoords("Invalid coords")


class InvalidCoords(ValueError):
    pass


# def is_valid_coords(c: "Coords") -> BoolLike:
def is_valid_coords(c: "Coords") -> bool:
    if isinstance(c, (CoordsIdentity, CoordsConst)):
        return True
    if isinstance(c, CoordsComp):
        return is_valid_coords(c.rest)
    if isinstance(c, ComposeList):  # type: ignore
        return all(is_valid_coords(x) for x in c.components)
    # return not_true(f"Invalid coords type {type(c).__name__}")
    return False


class CCOMapValue(CoordsConcreteOp[object]):
    def _reduce_seq(self, seq: Sequence[object], /) -> object:
        return tuple(seq)

    def _reduce_const(self, value: object, /) -> object:
        # vu = check_isinstance(value, ValueWithUnits)
        return vu.value  # type: ignore

    def _slice(self, x: Any, i: int, ntot: int, /) -> object:
        assert isinstance(x, tuple)
        if ntot is not None:
            n = len(x)  # type: ignore
            if n != ntot:
                raise ValueError(f"Expected {ntot} elements, got {n}")

        return x[i]  # type: ignore
