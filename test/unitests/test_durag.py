from test.constants import (
    DECIMALS,
)

def test_init(w3, DURAG):
    a0, a1 = w3.eth.accounts[:2]
    assert DURAG.name() == 'Durag Wave Edition 0'
    assert DURAG.symbol() == 'DURAG'
    assert DURAG.decimals() == 18
    assert DURAG.totalSupply() == 500*DECIMALS
    assert DURAG.balanceOf(a0) == 500*DECIMALS
    assert DURAG.balanceOf(a1) == 0

def test_transfer(w3, DURAG):
    a0, a1 = w3.eth.accounts[:2]
    DURAG.transfer(a1, 1*10**18, transact={})
    assert DURAG.balanceOf(a0) == 500*DECIMALS - 1*DECIMALS
    assert DURAG.balanceOf(a1) == 1*DECIMALS

def test_transferFrom(w3, DURAG):
    a0, a1, a2 = w3.eth.accounts[:3]
    assert DURAG.allowance(a0, a1) == 0
    DURAG.approve(a1, 1*DECIMALS, transact={})
    assert DURAG.allowance(a0, a1) == 1*DECIMALS
    DURAG.transferFrom(a0, a2, 1*DECIMALS, transact={'from': a1})
    assert DURAG.allowance(a0, a1) == 0
    assert DURAG.balanceOf(a0) == 500*DECIMALS - 1*DECIMALS
    assert DURAG.balanceOf(a1) == 0
    assert DURAG.balanceOf(a2) == 1*DECIMALS

def test_burn(w3, DURAG):
    a0, a1, a2 = w3.eth.accounts[:3]
    DURAG.burn(1*10**18, transact={})
    assert DURAG.balanceOf(a0) == 500*DECIMALS - 1*DECIMALS
    assert DURAG.totalSupply() == 500*DECIMALS - 1*DECIMALS

def test_burnFrom(w3, DURAG):
    a0, a1, a2 = w3.eth.accounts[:3]
    DURAG.approve(a1, 1*DECIMALS, transact={})
    DURAG.burnFrom(a0, 1*10**18, transact={'from': a1})
    assert DURAG.balanceOf(a0) == 500*DECIMALS - 1*DECIMALS
    assert DURAG.totalSupply() == 500*DECIMALS - 1*DECIMALS
