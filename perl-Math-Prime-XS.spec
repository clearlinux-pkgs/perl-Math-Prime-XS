#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Prime-XS
Version  : 0.27
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-Prime-XS-0.27.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-Prime-XS-0.27.tar.gz
Summary  : 'Detect and calculate prime numbers with deterministic tests'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Math-Prime-XS-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(boolean)

%description
NAME
Math::Prime::XS - Detect and calculate prime numbers with deterministic
tests

%package dev
Summary: dev components for the perl-Math-Prime-XS package.
Group: Development
Requires: perl-Math-Prime-XS-lib = %{version}-%{release}
Provides: perl-Math-Prime-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-Math-Prime-XS package.


%package lib
Summary: lib components for the perl-Math-Prime-XS package.
Group: Libraries

%description lib
lib components for the perl-Math-Prime-XS package.


%prep
%setup -q -n Math-Prime-XS-0.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Math/Prime/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Prime::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Math/Prime/XS/XS.so
