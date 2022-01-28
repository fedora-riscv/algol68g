%ifarch %{ix86} x86_64 ia64 ppc64le
%bcond_without libquadmath
%else
%bcond_with libquadmath
%endif

Name: algol68g
Summary: Algol 68 Genie compiler-interpreter
Version: 3.0.3
Release: 1%{?dist}
License: GPLv3+
URL: https://jmvdveer.home.xs4all.nl/en.algol-68-genie.html
Source: https://jmvdveer.home.xs4all.nl/%{name}-%{version}.tar.gz
Patch0: algol68g-cflags.patch
Patch1: algol68g-includedir.patch
Patch2: algol68g-libpq-include.patch
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(libRmath)
BuildRequires: pkgconfig(mpfr)
BuildRequires: pkgconfig(libpq)
%if %{with libquadmath}
BuildRequires: libquadmath-devel
%endif
BuildRequires: plotutils-devel

%description
Algol 68 Genie (Algol68G) is an Algol 68 compiler-interpreter.
It can be used for executing Algol 68 programs or scripts.
Algol 68 is a rather lean orthogonal general-purpose language
that is a beautiful means for denoting algorithms.
Algol 68 was designed as a general-purpose programming language
by IFIP Working Group 2.1 (Algorithmic Languages and Calculi)
that has continuing responsibility for Algol 60 and Algol 68.

%prep
%autosetup -p1

%build
autoreconf
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%{_bindir}/a68g
%{_mandir}/man1/a68g.1*
%license COPYING LICENSE
%doc AUTHORS NEWS README ChangeLog
%exclude %{_includedir}
%exclude %{_pkgdocdir}/COPYING
%exclude %{_pkgdocdir}/LICENSE

%changelog
* Wed Jan 26 2022 Oleg Girko <ol@infoserver.lv> - 3.0.3-1
- Update to 3.0.3
- Fix download URL to use HTTPS
- Use more specific file names in %%files section
- Don't put license files in docs
- Require gcc for build explicitly
* Mon Jan 24 2022 Oleg Girko <ol@infoserver.lv> - 3.0.2-1
- Update to 3.0.2
* Wed Jan 12 2022 Oleg Girko <ol@infoserver.lv> - 3.0.0-3
- Fix typo (source specified twice)
* Wed Jan 12 2022 Oleg Girko <ol@infoserver.lv> - 3.0.0-2
- Use libquadmath only on architectures that have it
* Wed Jan 12 2022 Oleg Girko <ol@infoserver.lv> - 3.0.0-1
- Initial package