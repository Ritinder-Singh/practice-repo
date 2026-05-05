-- TOPIC: Advanced Haskell | ghci: :load 08_advanced.hs
-- {-# LANGUAGE RankNTypes, DataKinds, GADTs, TypeFamilies, OverloadedStrings #-}

-- TODO 1: Type families — associated types and type functions
-- {-# LANGUAGE TypeFamilies #-}
-- type family Elem c where
--   Elem [a]    = a
--   Elem (Set a) = a
-- class Container c where
--   elements :: c -> [Elem c]

-- TODO 2: Data Kinds — promote values to types
-- {-# LANGUAGE DataKinds, KindSignatures #-}
-- data Nat = Zero | Succ Nat
-- data Vec :: Nat -> * -> * where
--   Nil  :: Vec 'Zero a
--   Cons :: a -> Vec n a -> Vec ('Succ n) a
-- -- Vec 'Zero Int  and  Vec ('Succ 'Zero) Int  are different types!

-- TODO 3: Phantom types — type parameters that don't appear in values
-- newtype Tagged t a = Tagged { untag :: a }
-- newtype Dollars = Dollars Double
-- newtype Euros   = Euros   Double
-- addDollars :: Tagged "USD" Double -> Tagged "USD" Double -> Tagged "USD" Double
-- addDollars (Tagged x) (Tagged y) = Tagged (x + y)
-- -- addDollars (Tagged 5 :: Tagged "USD" Double) (Tagged 3 :: Tagged "EUR" Double) -- TYPE ERROR

-- TODO 4: RankNTypes — higher-rank polymorphism
-- {-# LANGUAGE RankNTypes #-}
-- applyToInt :: (forall a. Show a => a -> String) -> String
-- applyToInt f = f (42 :: Int)
--
-- -- runST uses rank-2 types to prevent state from escaping:
-- -- runST :: (forall s. ST s a) -> a

-- TODO 5: Template Haskell — compile-time metaprogramming
-- {-# LANGUAGE TemplateHaskell #-}
-- import Language.Haskell.TH
-- -- $(makeFields ''MyRecord)     -- generates lenses
-- -- $(deriveJSON defaultOptions ''MyType)  -- generates JSON instances
-- -- listE [litE (integerL n) | n <- [1..10]]  -- splice list at compile time

-- TODO 6: Lenses — composable getters/setters
-- import Control.Lens
-- data Person = Person { _name :: String, _age :: Int } deriving (Show)
-- makeLenses ''Person  -- generates name and age lenses
--
-- alice :: Person
-- alice = Person "Alice" 30
-- view name alice           -- "Alice"
-- set  age  31 alice        -- Person { _name = "Alice", _age = 31 }
-- over name (map toUpper) alice  -- Person { _name = "ALICE", ... }

-- TODO 7: Coerce and Safe coerce
-- import Data.Coerce
-- newtype Name = Name String
-- newtype Email = Email String
-- nameToString :: Name -> String
-- nameToString = coerce  -- zero-cost, same representation

-- TODO 8: Recursion schemes — generic recursion patterns
-- import Data.Functor.Foldable
-- data ExprF r = NumF Int | AddF r r | MulF r r
-- type Expr = Fix ExprF
--
-- evalAlg :: ExprF Int -> Int
-- evalAlg (NumF n)   = n
-- evalAlg (AddF a b) = a + b
-- evalAlg (MulF a b) = a * b
--
-- eval :: Expr -> Int
-- eval = cata evalAlg  -- catamorphism (fold)
