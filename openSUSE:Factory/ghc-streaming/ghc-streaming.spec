#
# spec file for package ghc-streaming
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global pkg_name streaming
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.3.1
Release:        0
Summary:        An elementary streaming prelude and general stream type
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
%endif

%description
This package contains two modules,
<http://hackage.haskell.org/package/streaming/docs/Streaming.html Streaming>
and <http://hackage.haskell.org/package/streaming/docs/Streaming-Prelude.html
Streaming.Prelude>. The principal module,
<http://hackage.haskell.org/package/streaming-0.1.4.3/docs/Streaming-Prelude.html
Streaming.Prelude>, exports an elementary streaming prelude focused on a simple
"source" or "producer" type, namely 'Stream (Of a) m r'. This is a sort of
effectful version of '([a],r)' in which successive elements of type 'a' arise
from some sort of monadic action before the succession ends with a value of
type 'r'. Everything in the library is organized to make programming with this
type as simple as possible, by the simple expedient of making it as close to
'Prelude' and 'Data.List' as possible. Thus for example the trivial program

> >>> S.sum $ S.take 3 (S.readLn :: Stream (Of Int) IO ()) > 1<Enter> >
2<Enter> > 3<Enter> > 6 :> ()

sums the first three valid integers from user input. Similarly,

> >>> S.stdoutLn $ S.map (map toUpper) $ S.take 2 S.stdinLn > hello<Enter> >
HELLO > world!<Enter> > WORLD!

upper-cases the first two lines from stdin as they arise, and sends them to
stdout. And so on, with filtering, mapping, breaking, chunking, zipping,
unzipping, replicating and so forth: we program with streams of 'Int's or
'String's directly as if they constituted something like a list.
That's because streams really do constitute something like a list, and the
associated operations can mostly have the same names. (A few, like 'reverse',
don't stream and thus disappear; others like 'unzip' are here given properly
streaming formulation for the first time.) And we everywhere oppose "extracting
a pure list from IO", which is the origin of typical Haskell memory
catastrophes. Basically any case where you are tempted to use 'mapM',
'replicateM', 'traverse' or 'sequence' with Haskell lists, you would do better
to use something like 'Stream (Of a) m r'. The type signatures are a little
fancier, but the programs themselves are mostly the same. /In fact, they are
mostly simpler./ Thus, consider the trivial demo program mentioned in
<http://stackoverflow.com/questions/24068399/haskell-performance-of-iorefs this
SO question>

> main = mapM newIORef [1..10^8::Int] >>= mapM readIORef >>= mapM_ print

The new user notices that this exhausts memory, and worries about the
efficiency of Haskell 'IORefs'. But of course it exhausts memory! Look what it
says! The problem is immediately cured by writing

> main = S.print $ S.mapM readIORef $ S.mapM newIORef $ S.each [1..10^8::Int]

which really does what the other program was meant to do, uses no more memory
than 'hello-world', /and is simpler anyway/, since it doesn't involve the
detour of "extracting a list from IO". Almost every use of list 'mapM',
'replicateM', 'traverse' and 'sequence' produces this problem on a smaller
scale. People get used to it, as if it were characteristic of Haskell programs
to use a lot of memory. But in truth "extracting a list or sequence from IO" is
mostly just bad practice pure and simple. Of course, 'mapM', 'replicateM',
'traverse' and 'sequence' make sense for lists, under certain conditions! But
'unsafePerformIO' also makes sense under certain conditions.

The <http://hackage.haskell.org/package/streaming-0.1.4.3/docs/Streaming.html
Streaming> module exports the general type, 'Stream f m r', which can be used
to stream successive distinct steps characterized by /any/ functor 'f', though
we are mostly interested in organizing computations of the form 'Stream (Of a)
m r'. The streaming-IO libraries have various devices for dealing with
effectful variants of '[a]' or '([a],r)' in which the emergence of successive
elements somehow depends on IO. But it is only with the general type 'Stream f
m r', or some equivalent, that one can envisage (for example) the connected
streaming of their sorts of stream - as one makes lists of lists in the Haskell
'Prelude' and 'Data.List'. One needs some such type if we are to express
properly streaming equivalents of e.g.

> group :: Ord a => [a] -> [[a]] > chunksOf :: Int -> [a] -> [[a]] > lines ::
[Char] -> [[Char]] -- but similarly with byte streams, etc.

to mention a few obviously desirable operations. (This is explained more
elaborately in the <https://hackage.haskell.org/package/streaming#readme
readme> below.)

One could of course throw something like the present 'Stream' type on top of a
prior stream concept: this is how 'pipes' and 'pipes-group' (which are very
much our model here) use 'FreeT'. But once one grasps the iterable stream
concept needed to express those functions then one will also see that, with it,
one is /already/ in possession of a complete elementary streaming library -
since one possesses 'Stream ((,) a) m r' or equivalently 'Stream (Of a) m r'.
This is the type of a 'generator' or 'producer' or 'source' or whatever you
call an effectful stream of items. /The present Streaming.Prelude is thus the
simplest streaming library that can replicate anything like the API of the
Prelude and Data.List/.

The emphasis of the library is on interoperation; for the rest its advantages
are: extreme simplicity, re-use of intuitions the user has gathered from
mastery of 'Prelude' and 'Data.List', and a total and systematic rejection of
type synonyms. The two conceptual pre-requisites are some comprehension of
monad transformers and some familiarity with 'rank 2 types'. It is hoped that
experimentation with this simple material, starting with the ghci examples in
'Streaming.Prelude', will give people who are new to these concepts some
intuition about their importance. The most fundamental purpose of the library
is to express elementary streaming ideas without reliance on a complex
framework, but in a way that integrates transparently with the rest of Haskell,
using ideas - e.g. rank 2 types, which are here implicit or explicit in most
mapping - that the user can carry elsewhere, rather than chaining her
understanding to the curiosities of a so-called streaming IO framework (as
necessary as that is for certain purposes.)

See the <https://hackage.haskell.org/package/streaming#readme readme> below for
further explanation, including the examples linked there. Elementary usage can
be divined from the ghci examples in 'Streaming.Prelude' and perhaps from this
rough beginning of a
<https://github.com/michaelt/streaming-tutorial/blob/master/tutorial.md
tutorial>. Note also the
<https://hackage.haskell.org/package/streaming-bytestring streaming bytestring>
and <https://hackage.haskell.org/package/streaming-utils streaming utils>
packages. Questions about usage can be put raised on StackOverflow with the tag
'[haskell-streaming]', or as an issue on Github, or on the
<https://groups.google.com/forum/#!forum/haskell-pipes pipes list> (the package
understands itself as part of the pipes 'ecosystem'.)

The simplest form of interoperation with
<http://hackage.haskell.org/package/pipes pipes> is accomplished with this
isomorphism:

> Pipes.unfoldr Streaming.next :: Stream (Of a) m r -> Producer a m r >
Streaming.unfoldr Pipes.next :: Producer a m r -> Stream (Of a) m r

Interoperation with <http://hackage.haskell.org/package/io-streams io-streams>
is thus:

> Streaming.reread IOStreams.read :: InputStream a -> Stream (Of a) IO () >
IOStreams.unfoldM Streaming.uncons :: Stream (Of a) IO () -> IO (InputStream a)

With <http://hackage.haskell.org/package/conduit conduit> one might use, e.g.:

> Conduit.unfoldM Streaming.uncons :: Stream (Of a) m () -> Source m a > str ->
Streaming.mapM_ Conduit.yield (hoist lift str) :: Stream (Of o) m r -> ConduitM
i o m r > src -> hoist lift str $$ Conduit.mapM_ Streaming.yield :: Source m a
-> Stream (Of a) m ()

These conversions should never be more expensive than a single '>->' or '=$='.
The simplest interoperation with regular Haskell lists is provided by, say

> Streaming.each :: [a] -> Stream (Of a) m () > Streaming.toList_ :: Stream (Of
a) m r -> m [a]

The latter of course accumulates the whole list in memory, and is mostly what
we are trying to avoid. Every use of 'Prelude.mapM f' should be reconceived as
using the composition 'Streaming.toList_ . Streaming.mapM f .
Streaming.each' with a view to considering whether the accumulation required by
'Streaming.toList_' is really necessary.

Here are the results of some
<https://gist.github.com/michaelt/96606bbf05b29bf43a05aba081dc9bd4#file-benchmachines-hs
microbenchmarks> based on the
<https://github.com/ekmett/machines/blob/master/benchmarks/Benchmarks.hs
benchmarks> included in the machines package:

<<http://i.imgur.com/YbQtlXm.png>>

Because these are microbenchmarks for individual functions, they represent a
sort of "worst case"; many other factors can influence the speed of a complex
program.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc README.md changelog.md

%changelog
